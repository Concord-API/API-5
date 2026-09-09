# Definition of Done (DoD)
### Código e testes

- Código implementado e revisado por outro membro do time.
- Testes automatizados criados e executados (unitários e de integração), todos verdes no pipeline.
- Funcionalidades críticas cobertas por teste: cálculo da nota, agregações e regras de exibição de procedência.

### Dados e pipeline

- Migrations versionadas e aplicadas pelo runner no pipeline; nenhum SQL executado à mão em produção.
- Carga idempotente comprovada: a mesma carga rodada duas vezes não duplica linha nem infla contagem.
- O ETL roda de forma independente da API, como job agendado em horário de baixo uso.
- As perguntas do item são respondidas por consulta OLAP pré-agregada, não por agregação sobre a tabela fato em tempo de request.

### Produto

- Todo dado exibido, analítico ou descritivo, traz fonte, data de extração, escopo e método de apuração.
- O escopo TJSP, TJRJ e TJMG está visível na tela.
- Estado vazio tratado: a tela informa o que não existe e por quê, sem campo em branco nem valor plausível inventado.
- Documentação mínima atualizada (README, dicionário de dados, grão das tabelas).
- Incremento demonstrável em ambiente de homologação.
