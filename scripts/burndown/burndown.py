#!/usr/bin/env python3
"""Gera o burndown da sprint a partir do board do GitHub.

A fonte de verdade são os eventos de mudança de status do GitHub Projects e o
issue field `Horas`. Nada é lido de planilha, então o gráfico de qualquer dia
pode ser refeito depois, passando --hoje.

    python3 scripts/burndown/burndown.py
    python3 scripts/burndown/burndown.py --sprint "Sprint 1" --hoje 2026-09-24
"""

import argparse
import csv
import datetime
import json
import os
import re
import subprocess
import sys
from zoneinfo import ZoneInfo

REPO_OWNER = "Concord-API"
REPO_NAME = "API-5"
CAMPO_HORAS = "Horas"
CAMPO_SPRINT = "Sprint"
FUSO = ZoneInfo("America/Sao_Paulo")

AQUI = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(AQUI, "sprints.json")
SAIDA = os.path.normpath(os.path.join(AQUI, "..", "..", "Docs", "Scrum", "burndown"))

TINTA = "#14120F"
VERMELHO = "#A3121A"
META = "#8B8478"
FILETE = "#DCD6C9"
GRADE = "#EBE6DB"
PONTILHADO = "#C9C2B4"


def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("gh falhou: " + (r.stderr or r.stdout).strip())
    return r.stdout


def graphql(query):
    corpo = json.loads(gh("api", "graphql", "-f", "query=" + query))
    if "errors" in corpo:
        sys.exit("GraphQL: " + json.dumps(corpo["errors"], ensure_ascii=False)[:400])
    return corpo["data"]


def dia_local(instante):
    utc = datetime.datetime.fromisoformat(instante.replace("Z", "+00:00"))
    return utc.astimezone(FUSO).date()


def escolher_sprint(sprints, nome, hoje):
    if nome:
        achada = [s for s in sprints if s["nome"] == nome]
        if not achada:
            sys.exit(f"sprint {nome!r} não está em sprints.json")
        return achada[0]
    for s in sprints:
        if s["abertura"] <= hoje.isoformat() <= s["fim"]:
            return s
    return None


def coletar(sprint):
    listagem = json.loads(gh("issue", "list", "-R", f"{REPO_OWNER}/{REPO_NAME}",
                             "--limit", "1000", "--state", "all",
                             "--json", "number,title"))
    numeros = [i["number"] for i in listagem if re.match(r"^\d+\.\d+\s", i["title"])]

    fragmento = """{
      number
      issueFieldValues(first:20){nodes{
        ... on IssueFieldNumberValue{value field{... on IssueFieldNumber{name}}}
        ... on IssueFieldSingleSelectValue{name field{... on IssueFieldSingleSelect{name}}}
      }}
      timelineItems(last:100,itemTypes:[PROJECT_V2_ITEM_STATUS_CHANGED_EVENT]){
        nodes{... on ProjectV2ItemStatusChangedEvent{createdAt status}}
      }
    }"""

    tasks = {}
    for i in range(0, len(numeros), 20):
        consulta = ('{repository(owner:"%s",name:"%s"){' % (REPO_OWNER, REPO_NAME)
                    + " ".join(f"i{n}:issue(number:{n})" + fragmento
                               for n in numeros[i:i + 20])
                    + "}}")
        for no in graphql(consulta)["repository"].values():
            campos = {}
            for v in no["issueFieldValues"]["nodes"]:
                if v.get("field", {}).get("name"):
                    campos[v["field"]["name"]] = v.get("value", v.get("name"))
            if campos.get(CAMPO_SPRINT) != sprint:
                continue
            tasks[no["number"]] = {
                "horas": campos.get(CAMPO_HORAS) or 0,
                "eventos": [(dia_local(e["createdAt"]), e["status"])
                            for e in no["timelineItems"]["nodes"] if e],
            }
    return tasks


def status_em(eventos, dia):
    ate = [s for d, s in eventos if d <= dia]
    return ate[-1] if ate else None


def serie(tasks, inicio, fim, hoje):
    total = sum(t["horas"] for t in tasks.values())
    dias = [inicio + datetime.timedelta(d) for d in range((fim - inicio).days + 1)]
    linhas = []
    for i, dia in enumerate(dias):
        feito = sum(t["horas"] for t in tasks.values()
                    if status_em(t["eventos"], dia) == "Done")
        passado = dia <= hoje
        linhas.append({
            "data": dia,
            "restante": total - feito if passado else None,
            "feito": feito if passado else None,
            "ideal": round(total * (1 - i / (len(dias) - 1))),
        })
    return total, linhas


def passo_da_grade(total):
    for passo in (25, 50, 100, 200):
        if total / passo <= 5:
            return passo
    return 500


def svg(total, linhas, tasks, sprint, hoje, nota):
    L, T, W, H = 64, 92, 576, 280
    n = len(linhas) - 1
    x = lambda i: L + i * W / n
    y = lambda v: T + H * (1 - v / total)

    reais = [(x(i), y(l["restante"])) for i, l in enumerate(linhas)
             if l["restante"] is not None]
    if not reais:
        reais = [(x(0), y(total))]
    ideais = " ".join(f"{x(i):.1f},{y(l['ideal']):.1f}" for i, l in enumerate(linhas))
    ux, uy = reais[-1]
    restante = next((l["restante"] for l in reversed(linhas)
                     if l["restante"] is not None), total)
    dia_corte = min(hoje, linhas[-1]["data"])
    concluidas = sum(1 for t in tasks.values()
                     if status_em(t["eventos"], dia_corte) == "Done")

    passo = passo_da_grade(total)
    marcas = range(passo, int(total) + 1, passo)
    grade = "".join(f'<line x1="{L}" y1="{y(v):.1f}" x2="{L+W}" y2="{y(v):.1f}"/>'
                    for v in marcas)
    rotulos_y = "".join(f'<text x="{L-8}" y="{y(v)+3.5:.1f}">{v}h</text>' for v in marcas)
    rotulos_x = "".join(f'<text x="{x(i):.1f}" y="{T+H+20}">{l["data"]:%d/%m}</text>'
                        for i, l in enumerate(linhas) if n <= 10 or i % 2 == 0 or i == n)
    marcos = "".join(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.5"/>' for px, py in reais[:-1])

    marca_hoje = ""
    idx = next((i for i, l in enumerate(linhas) if l["data"] == hoje), None)
    if idx is not None:
        hx = x(idx)
        marca_hoje = (f'<line x1="{hx:.1f}" y1="{T}" x2="{hx:.1f}" y2="{T+H}" stroke="{PONTILHADO}" '
                      f'stroke-width="1" stroke-dasharray="2 4"/>'
                      f'<text x="{hx+6:.1f}" y="{T+8}" font-size="9" fill="{META}">HOJE</text>')

    ancora, tx = ("end", ux - 16) if ux > L + W * 0.7 else ("start", ux + 16)
    ty = uy - 34 if uy > T + H - 70 else uy + 32
    halo = 'paint-order="stroke" stroke="#FFFFFF" stroke-width="3.5"'

    inicio, fim = linhas[0]["data"], linhas[-1]["data"]
    rodape = [nota] if nota else []
    rodape += [f"Fonte: eventos de mudança de status do GitHub Projects ({REPO_OWNER}/{REPO_NAME}),",
               f"ponderados pelo campo {CAMPO_HORAS} de cada task. Extração de {hoje:%d/%m/%Y}."]
    textos = "".join(f'<text x="48" y="{436 + 12*i}">{t}</text>' for i, t in enumerate(rodape))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 {440 + 12*len(rodape)}" width="780" height="{440 + 12*len(rodape)}" font-family="'IBM Plex Mono', ui-monospace, monospace">
  <rect width="100%" height="100%" fill="#FFFFFF"/>
  <text x="48" y="40" font-family="'Source Serif 4', Georgia, serif" font-size="21" font-weight="700" fill="{TINTA}">Burndown — {sprint}</text>
  <text x="48" y="60" font-size="11" fill="{META}">Ratio · {len(tasks)} tasks · {total:g}h · acompanhamento de {inicio:%d/%m} a {fim:%d/%m/%Y}</text>
  <g stroke="{GRADE}" stroke-width="1">{grade}</g>
  <line x1="{L}" y1="{T+H}" x2="{L+W}" y2="{T+H}" stroke="{FILETE}" stroke-width="1"/>
  <g font-size="10" fill="{META}" text-anchor="end">{rotulos_y}<text x="{L-8}" y="{T+H+3.5}">0</text></g>
  <g font-size="10" fill="{META}" text-anchor="middle">{rotulos_x}</g>
  {marca_hoje}
  <polyline points="{ideais}" fill="none" stroke="{META}" stroke-width="2" stroke-dasharray="6 5"/>
  <text x="{L+W+10}" y="{T+H+3}" font-size="10" fill="{META}">ideal</text>
  <polyline points="{" ".join(f"{px:.1f},{py:.1f}" for px, py in reais)}" fill="none" stroke="{VERMELHO}" stroke-width="2"/>
  <g fill="#FFFFFF" stroke="{VERMELHO}" stroke-width="2">{marcos}</g>
  <circle cx="{ux:.1f}" cy="{uy:.1f}" r="5.5" fill="{VERMELHO}" stroke="#FFFFFF" stroke-width="2"/>
  <text x="{L+10}" y="{T-6}" font-size="10" fill="{META}">{total:g}h</text>
  <text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{ancora}" font-size="11" font-weight="600" fill="{VERMELHO}" {halo}>{restante:g}h restantes</text>
  <text x="{tx:.1f}" y="{ty+14:.1f}" text-anchor="{ancora}" font-size="10" fill="{META}" {halo}>{concluidas} de {len(tasks)} tasks concluídas</text>
  <line x1="48" y1="420" x2="732" y2="420" stroke="{FILETE}" stroke-width="1"/>
  <g font-size="9.5" fill="{META}">{textos}</g>
</svg>
'''


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sprint", help="nome da sprint; sem ele, a sprint em curso hoje")
    p.add_argument("--hoje", help="AAAA-MM-DD; sem ele, a data de hoje em São Paulo")
    a = p.parse_args()

    hoje = (datetime.date.fromisoformat(a.hoje) if a.hoje
            else datetime.datetime.now(FUSO).date())
    with open(CONFIG, encoding="utf-8") as f:
        sprints = json.load(f)["sprints"]
    cfg = escolher_sprint(sprints, a.sprint, hoje)
    if cfg is None:
        print(f"{hoje:%d/%m/%Y} não cai em nenhuma sprint de sprints.json; nada a gerar.")
        return

    tasks = coletar(cfg["nome"])
    total, linhas = serie(tasks, datetime.date.fromisoformat(cfg["inicio"]),
                          datetime.date.fromisoformat(cfg["fim"]), hoje)
    if not tasks or total == 0:
        sys.exit(f"nenhuma task com {CAMPO_SPRINT} = {cfg['nome']} e {CAMPO_HORAS} preenchido")

    base = cfg["nome"].lower().replace(" ", "-")
    os.makedirs(os.path.join(SAIDA, "historico"), exist_ok=True)
    grafico = svg(total, linhas, tasks, cfg["nome"], hoje, cfg.get("nota"))
    for caminho in (os.path.join(SAIDA, f"{base}.svg"),
                    os.path.join(SAIDA, "historico", f"{base}-{hoje.isoformat()}.svg")):
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(grafico)
    with open(os.path.join(SAIDA, f"{base}.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["data", "restante_real_h", "ideal_h", "concluido_h"])
        for l in linhas:
            w.writerow([l["data"].isoformat(),
                        "" if l["restante"] is None else f"{l['restante']:g}",
                        l["ideal"],
                        "" if l["feito"] is None else f"{l['feito']:g}"])

    atual = next((l for l in reversed(linhas) if l["restante"] is not None), None)
    print(f"{cfg['nome']} · {len(tasks)} tasks · {total:g}h"
          + (f" · restante {atual['restante']:g}h em {atual['data']:%d/%m}" if atual else ""))


if __name__ == "__main__":
    main()
