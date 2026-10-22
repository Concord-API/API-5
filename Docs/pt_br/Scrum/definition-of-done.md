# Definition of Done (DoD)

Uma história só está pronta quando cada item abaixo foi verificado no nível indicado, por
quem está indicado.

| Nível | O que acontece nele |
| --- | --- |
| **PR da task** | PR de uma task para a `us0` ou para a `usX`: formatação, lint, build, testes unitários e de integração e análise do Sonar |
| **Acceptance** | push na `us0` ou na `usX`: a aplicação é instalada em Windows Server atrás do IIS, sobe num banco vazio, recebe a carga de amostra e responde busca e detalhe do tema pelo IIS |
| **PR `usX → main`** | revisão de código, label de release, *quality gate* do Sonar sobre o código da história e checklist de QA da história |
| **Push na `main`** | CI e *quality gate* do Sonar sobre o código integrado; a release só é publicada com tudo verde |
| **Carga** | geração do arquivo de carga, do nosso lado |
| **Homologação** | demonstração do incremento ao PO |

### Código e testes

| Item | Onde é verificado | Quem verifica |
| --- | --- | --- |
| Código implementado e revisado por outra pessoa do time. | PR `usX → main` | Code Reviewers |
| Testes automatizados escritos e executados (unitários e de integração), todos verdes no pipeline. | PR da task | autor da task |
| Comportamento crítico coberto por teste: cálculo do score, agregações e as regras de exibição de procedência. | PR da task (cobertura no Sonar) e PR `usX → main` (revisão) | autor da task e Code Reviewers |
| *Quality gate* do SonarQube Cloud (Sonar way) verde sobre o código novo: confiabilidade, segurança e manutenibilidade nota A, cobertura de ao menos 80%, duplicação de no máximo 3% e todos os *security hotspots* revisados. | PR `usX → main` e push na `main` | CI |

### Dados e pipeline

| Item | Onde é verificado | Quem verifica |
| --- | --- | --- |
| O schema do `dw` muda só por migração versionada, aplicada pela API quando ela sobe; nenhum DDL é executado à mão em nenhum ambiente. | Acceptance | CI |
| Carga idempotente comprovada: a mesma carga executada duas vezes não duplica nenhuma linha nem infla nenhuma contagem. | PR da task | autor da task |
| A carga roda do nosso lado, manualmente e independente da API; homologação e produção recebem só o arquivo de carga gerado por ela, com os testes de integridade vazios. | Carga | responsável pela carga |
| As perguntas do item são respondidas por uma consulta OLAP pré-agregada, e não por agregação sobre a tabela fato no momento da requisição. | PR `usX → main` | Code Reviewers |

### Produto

| Item | Onde é verificado | Quem verifica |
| --- | --- | --- |
| Todo valor exibido, analítico ou descritivo, carrega sua fonte, data de extração, escopo e como foi calculado. | PR `usX → main` (checklist de QA) | autor da história |
| O escopo TJSP, TJRJ, TJMG, STJ e STF está visível na tela. | PR `usX → main` (checklist de QA) | autor da história |
| Estado vazio tratado: a tela declara o que não existe e por quê, sem campo em branco e sem valor plausível inventado. | PR `usX → main` (checklist de QA) | autor da história |
| Documentação mínima atualizada (README, dicionário de dados, grão da tabela). | PR `usX → main` | Code Reviewers |
| Incremento demonstrável no ambiente de homologação, instalado em Windows Server atrás do IIS da mesma forma que estará no servidor do cliente. | Acceptance (instalação) e Homologação (demonstração) | CI e PO |

### Build vermelho

Se o CI ou o Acceptance ficar vermelho na `us0`, numa `usX` ou na `main`, quem fez o
último merge reverte esse merge primeiro e investiga depois. Ninguém mergeia em cima de
uma branch vermelha.

Um *quality gate* do Sonar vermelho no push da `main` deixa o CI da `main` vermelho, e a
release daquele merge não é publicada.
