# Definition of Done (DoD)

### Código e testes

- Código implementado e revisado por outra pessoa do time.
- Testes automatizados escritos e executados (unitários e de integração), todos verdes no pipeline.
- Comportamento crítico coberto por teste: cálculo do score, agregações e as regras de exibição de procedência.

### Dados e pipeline

- O schema do `dw` muda só por migração versionada, aplicada pela API quando ela sobe; nenhum DDL é executado à mão em nenhum ambiente.
- Carga idempotente comprovada: a mesma carga executada duas vezes não duplica nenhuma linha nem infla nenhuma contagem.
- A carga roda do nosso lado, manualmente e independente da API; homologação e produção recebem só o arquivo de carga gerado por ela, com os testes de integridade vazios.
- As perguntas do item são respondidas por uma consulta OLAP pré-agregada, e não por agregação sobre a tabela fato no momento da requisição.

### Produto

- Todo valor exibido, analítico ou descritivo, carrega sua fonte, data de extração, escopo e como foi calculado.
- O escopo TJSP, TJRJ, TJMG, STJ e STF está visível na tela.
- Estado vazio tratado: a tela declara o que não existe e por quê, sem campo em branco e sem valor plausível inventado.
- Documentação mínima atualizada (README, dicionário de dados, grão da tabela).
- Incremento demonstrável no ambiente de homologação, instalado em Windows Server atrás do IIS da mesma forma que estará no servidor do cliente.