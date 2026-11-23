# Modelo de tasks

Como o trabalho do time é registrado no board **API V Tasks**: o que é uma user story, o que é
uma task, onde fica o trabalho que não pertence a nenhuma história e como cada item é escrito.
O critério para uma história entrar na Sprint está na [DoR](definition-of-ready.md), e o critério
para ela sair, na [DoD](definition-of-done.md).

## Hierarquia

Todo item do board está em um destes dois lugares:

- **Uma user story** (`US-XX`), com as suas tasks como sub-issues. As tasks são o trabalho de verdade:
  é nelas que ficam o responsável e as horas.
- **Um container**, quando o trabalho não pertence a nenhuma história. São dois:
  [Technical Foundation](#technical-foundation) e [DevOps](#devops).

O ID de cada item é único no projeto inteiro e nunca é renumerado, porque ele vai no nome da
branch (veja [Branches](../README.md#branches)).

## Containers

### Technical Foundation

A base técnica do produto que não é uma user story: schema do Data Warehouse, pipeline,
esqueleto do frontend, dados de referência e investigações de fonte.

| | |
| --- | --- |
| ID das tasks | `0.Y` — o `0` ocupa o lugar do número da história (`0.12`, `0.113`) |
| Branch base | `us0` |
| Exemplos | `0.12 Create the dw schema migration and apply it on API startup`, `0.112 Spike: find a lawful source of court rulings with summary for the courts in scope` |

### DevOps

Tudo o que leva o produto do código até o servidor e o mantém funcionando: integração contínua,
deploy, qualidade, monitoramento, testes, banco de dados e a documentação disso.

| | |
| --- | --- |
| ID das tasks | `DVP-NN`, sequencial (`DVP-01`, `DVP-02`…) |
| Branch base | `us0`, a mesma do Technical Foundation |
| Frente | campo `Frente` do board: `CI`, `Deploy`, `QA`, `Monitoramento`, `Testes`, `BD` ou `Docs` |
| Exemplo | `DVP-75 Cache the search filter options until the next load` |

O DevOps não tem branch base própria. Uma task de DevOps que gera commit tem a sua branch de task,
criada a partir da `us0` e mergeada de volta nela, como as tasks `0.Y`. Uma branch base só para o
DevOps não teria o que integrar, porque cada task de DevOps é independente das outras.

Task de DevOps sem branch também é normal, por exemplo uma configuração feita fora do GitHub: ela
existe para registrar o trabalho e as horas, e o card é movido à mão.

## User story

- **Título:** `US-XX — ` seguido do texto completo da história em inglês, sem abreviar, igual ao
  sprint backlog.
- **Tipo:** `User Story`.
- **Campos:** `Priority`, `Effort (SP)` e `Sprint`. O corpo fica vazio.
- **Sem responsável e sem label de camada.** Quem faz a história são as tasks, e mais de uma pessoa
  pode trabalhar nas tasks de uma mesma história.

## Task

### ID e título

- **ID:** `X.Y`, em que `X` é o número da história (as tasks da US-01 são `1.1`, `1.2`…). Nos
  containers, `0.Y` ou `DVP-NN`.
- **Título:** curto, no imperativo e **em inglês**, sem tag de camada (a camada é o label).
  Exemplo: `39.9 Explain in the case view what does not exist and why`.

### Descrição

Só quando o título não basta. Em linhas soltas, nunca em parágrafo, cada uma começando por um
destes rótulos:

| Rótulo | O que diz |
| --- | --- |
| `Data:` | o campo, a regra ou o dado que a task trata |
| `Message:` | o texto exato mostrado ao usuário |
| `Verifies:` | o que o teste ou o critério prova quando a task termina |
| `Depends:` | as tasks ou decisões de que ela depende |

O texto das linhas pode ser em português ou em inglês. O padrão rígido é só o título.

Exemplo:

```
39.9 Explain in the case view what does not exist and why

Data: caso ou tribunal sem dado carregado diz o que falta e por quê (US-26): sem campo vazio, sem enchimento, sem link
Message: TJRJ e TJMG: "Os dados deste processo não estão disponíveis no Ratio: a consulta pública do {tribunal} só pode ser feita com captcha."
Depends: 39.6
```

### Horas

- Toda task tem horas no campo `Horas`, e **sempre menos de 8h**.
- Uma task que passa de 8h é quebrada em duas ou mais.

### Documentação

A documentação de uma task é **uma task própria**, com label `Docs`, a mesma frente e o mesmo
responsável, e `Depends:` apontando para a task que ela documenta. Assim as horas de escrever não
inflam as da task técnica.

### Campos

| Campo | Valor |
| --- | --- |
| Tipo | `Task` |
| Responsável | quem faz a task |
| Label | a camada do trabalho: `Backend`, `Frontend`, `ETL`, `Test`, `DevOps` ou `Docs` |
| `Sprint` | a Sprint em que a task é feita |
| `Horas` | a estimativa, abaixo de 8h |
| `Status` | `Todo` → `In Progress` → `Review` → `Done` |
| `Frente` | só nas tasks de DevOps |

`Priority` e `Effort (SP)` são só da user story.

Toda task nova nasce no board com `Status` em `Todo`. Uma issue criada fora do board e só depois
associada a ele fica sem status e não aparece em nenhuma coluna.

## Regra de ouro

Toda task responde, mesmo que implicitamente: ***o que precisa ser verdade depois que ela
terminar?*** Quem lê tem que conseguir julgar se ela está pronta sem voltar à DoR.
