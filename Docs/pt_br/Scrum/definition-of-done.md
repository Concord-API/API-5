# Definition of Done (DoD)

### Código e testes

- Código implementado e revisado por outra pessoa do time.
- Testes automatizados escritos e executados (unitários e de integração), todos verdes no pipeline.
- Comportamento crítico coberto por teste: cálculo do score, agregações e as regras de exibição de procedência.

### Dados e pipeline

- Migrações versionadas aplicadas pelo runner no pipeline; nenhum SQL executado à mão em produção.
- Carga idempotente comprovada: a mesma carga executada duas vezes não duplica nenhuma linha nem infla nenhuma contagem.
- O ETL roda independentemente da API, como job agendado em janela de baixo uso.
- As perguntas do item são respondidas por uma consulta OLAP pré-agregada, e não por agregação sobre a tabela fato no momento da requisição.

### Produto

- Todo valor exibido, analítico ou descritivo, carrega sua fonte, data de extração, escopo e como foi calculado.
- O escopo TJSP, TJRJ e TJMG está visível na tela.
- Estado vazio tratado: a tela declara o que não existe e por quê, sem campo em branco e sem valor plausível inventado.
- Documentação mínima atualizada (README, dicionário de dados, grão da tabela).
- Incremento demonstrável no ambiente de homologação, instalado em Windows Server atrás do IIS da mesma forma que estará no servidor do cliente.