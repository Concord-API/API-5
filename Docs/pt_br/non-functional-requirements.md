# Requisitos Não Funcionais

Aplicam-se a todas as histórias e são cobrados na
[Definition of Done](Scrum/definition-of-done.md).

## Dados e pipeline

| # | Requisito |
| --- | --- |
| NFR-01 | O dado é armazenado em um Data Warehouse com modelagem dimensional (tabela fato, dimensões e tabela ponte para relações N:N), com o grão declarado por escrito. |
| NFR-02 | Todo valor exibido, analítico ou descritivo, declara sua fonte e como foi calculado (para todo tema). |
| NFR-03 | Migrações versionadas, aplicadas por um runner no pipeline. Nunca SQL à mão em produção. |
| NFR-04 | Existe um pipeline de ETL completo, executável de forma independente dos demais componentes. |
| NFR-05 | A carga é idempotente: executá-la duas vezes com os mesmos dados não duplica nenhuma linha nem infla nenhuma contagem. |
| NFR-06 | O ETL roda como job agendado, fora do ciclo de vida da API, em janela de baixo uso. |
| NFR-07 | As perguntas do produto são respondidas por consultas OLAP pré-agregadas — sumário por tema, por ano, por tribunal, por câmara — atualizadas ao fim de cada carga, e não por agregação sobre a tabela fato no momento da requisição. |
| NFR-08 | A busca full-text é em português, dentro do Postgres, tolerando ausência de acentos e erros de digitação. |
| NFR-09 | A aplicação roda no Windows Server do cliente, dentro da intranet dele. Nenhum componente depende de serviço em nuvem para operar. |
| NFR-10 | A camada web é servida atrás do **IIS**, padrão atual do cliente, sem depender de recursos específicos do IIS — colocar o **NGINX** no mesmo servidor em seu lugar não pode exigir alteração na aplicação. |
| NFR-11 | O PostgreSQL roda no servidor do próprio cliente. Nenhum dado processual sai da rede dele. |
| NFR-12 | A aplicação funciona sem acesso à internet em tempo de execução. O **ETL é o único componente que precisa de acesso de saída**, por meio de allowlist de hosts ou proxy configurável; enquanto esse acesso estiver indisponível, o produto continua servindo os dados já carregados e declara sua data de extração. |
| NFR-15 | A capacidade necessária é declarada antes da instalação: CPU, RAM e disco, incluindo o crescimento vindo dos textos de decisão armazenados, para que o TI do cliente possa dimensionar o servidor. |
| NFR-16 | A aplicação é operável sem ferramental de nuvem: logs estruturados no servidor, uma sonda de liveness e uma de readiness que reporta a idade da última extração, e um alarme que chega a uma pessoa quando o ETL falha ou não roda em sua janela. |
| NFR-17 | O acesso é restrito à intranet — sem exposição à internet. |
| NFR-18 | Qualquer provedor externo de modelo de linguagem é **opcional e declarado**. Desabilitá-lo não quebra o restante da aplicação, e enquanto estiver habilitado há log de auditoria de toda conversa, política de retenção definida e teto de uso e custo por pergunta. |
| NFR-19 | Nenhum segredo no repositório: strings de conexão, chaves de API e credenciais vêm da configuração de ambiente no servidor do cliente. Uma variável obrigatória ausente faz a aplicação falhar imediatamente, nomeando a variável. |

## Idioma e conformidade

| # | Requisito |
| --- | --- |
| NFR-20 | Identificadores em inglês, valores de domínio em português. O texto visível ao usuário é em português, incluindo rótulos e mensagens de erro. |
| NFR-21 | LGPD e segredo de justiça: nenhum dado pessoal é indexado além do que a fonte oficial expõe, um processo em segredo de justiça é sinalizado e nunca exibido, e onde inteiros teores forem armazenados, os termos de uso de cada tribunal e os dados pessoais contidos nesses textos são verificados e registrados. |

---