
# Ratio 
> (latim: razão, fundamento). De ratio decidendi — o fundamento determinante de
> uma decisão judicial, aquilo que de fato se repete e vira padrão.

![home](assets/home.jpeg)

## Índice
- [Introdução](#introdução)
- [Principais Funcionalidades](#principais-funcionalidades)
- [Equipe](#equipe)
- [Como contribuir?](#como-contribuir)
  - [Branches](#branches)
  - [Commits](#commits)

## Introdução
O Ratio tem como objetivo eliminar o trabalho manual e fragmentado da análise jurisprudencial que impede advogados e magistrados de identificar com segurança o posicionamento dos tribunais sobre uma determinada tese, permitindo avaliar rapidamente sua aceitação, recorrência e grau de consolidação para embasar decisões e estratégias jurídicas, por meio da centralização e análise de jurisprudências, precedentes e doutrinas do TJSP, TJRJ e TJMG em um Data Warehouse jurídico, com busca semântica por tema e geração de indicadores e padrões de decisão rastreáveis às fontes originais.

## Principais Funcionalidades
- Busca por tema, em linguagem natural — o usuário descreve o caso com suas próprias palavras e recebe o tema jurídico já identificado, sem precisar montar sintaxe de busca ou saber o nome técnico da tese.
- Padrão de decisão consolidado — percentual de acolhimento, volume de processos e tribunais envolvidos, calculados automaticamente. Elimina a tabulação manual de decisões em planilha.
- Nota de força do entendimento — indica o quão consolidado (ou instável) é aquele padrão, considerando concordância entre decisões, volume, cobertura e recência.
- Rastreabilidade — cada número exibido leva de volta à sua fonte e à data de extração; nenhuma métrica é inventada ou calculada "no escuro".
- Cobertura multi-tribunal — dados centralizados de TJSP, TJRJ e TJMG, os três tribunais com maior volume processual do país.
- Acesso a precedentes e doutrina relacionados — afim de manter a rastreabilidade, é possível acessar a todos os precedentes e doutrinas relacionados que foram utilizados para sumarizar o tema.

## Equipe
<div align="center">
  <table>
    <thead>
      <tr>
        <th align="center">Integrante</th>
        <th align="center">Função</th>
        <th align="center">GitHub</th>
      </tr>
    </thead>
    <tbody>
          <tr>
        <td align="center">Vinicius de Pádua</td>
        <td align="center">Product Owner</td>
        <td align="center"><a href="https://github.com/orgs/vp-p"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">João Vitor Andrade</td>
        <td align="center">Scrum Master</td>
        <td align="center"><a href="https://github.com/joaoandrade17"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">João Vitor Baranov</td>
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/JoaoBaranov"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Victor Nogueira</td>
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/victorgsnogueira"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Richard Cordeiro</td>
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/RichardCordeiro"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Isaac Oliveira</td>
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/IsaacOliveiraSouza"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Thiago Abreu</td>
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/thiagosabreu"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
    </tbody>
  </table>
</div>

## Como contribuir?
### Branches
- **Feature Branching + branch por Sprint**
- **main:** Branch principal e estável do projeto. Recebe merges apenas ao final de cada sprint, após revisão e aprovação.
- **sprintX** (ex: sprint1, sprint2, sprint3): Cada sprint possui sua própria branch base, onde são integradas todas as funcionalidades desenvolvidas durante aquele ciclo.
- **taskpai-subtask-nome-da-task-com-traço-se-tiver-espaco:** Para cada nova funcionalidade ou correção, é criada uma branch específica a partir da branch da sprint em andamento. Essa Branch é criada com base na task do board. Exemplo: `RATIO-35-0.1-Implementar-documentação-API`
- **Repositório de documentação:** tendo em vista que as branches deste repositório não são ligadas a taks, devem seguir um padrão diferente. Deve apenas conter o nome da aplicação acompanhado da palavra “**DOCS**” e da descrição do que está sendo feito, por exemplo, `RATIO-DOCS-Definition-of-Done`, `RATIO-DOCS-Product-Backlog`
### Commits
**Todos os commits para qualquer repositório deste projeto devem ser feitos em inglês**  
Cada commit deve ser pequeno, descritivo e objetivo, seguindo o padrão de convenção semântica:

- `feat:` descrição da nova funcionalidade
- `fix:` correção de bug ou comportamento inesperador
- `factor:` melhoria de código sem alterar comportamento
- `docs:` atualização de documentação
- `chore:` tarefas de configuração, build ou manutenção

Exemplo: `feat: add semantic search by legal topic`

O número de commits é usado como indicador de contribuição individual e progresso da sprint, permitindo rastrear o fluxo de trabalho no repositório
