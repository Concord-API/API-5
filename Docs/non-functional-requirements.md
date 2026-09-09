# Requisitos não funcionais

Valem para todas as stories e estão refletidos no DoD acima.

| # | Requisito |
| --- | --- |
| RNF-01 | O dado é armazenado em Data Warehouse com modelagem dimensional (tabela fato, dimensões e tabela-ponte para relações N:N), com o grão declarado por escrito. |
| RNF-02 | Todo dado exibido, analítico ou descritivo, informa sua fonte e como foi formulado (para todos os temas). |
| RNF-03 | Migrations versionadas, aplicadas por runner no pipeline. Nunca SQL à mão em produção. |
| RNF-04 | Existe um pipeline de ETL completo, executável de forma independente das outras soluções. |
| RNF-05 | A carga é idempotente: rodar duas vezes com os mesmos dados não duplica linha nem infla contagem. |
| RNF-06 | O ETL roda como job agendado, fora do ciclo de vida da API, em horário de baixo uso. |
| RNF-07 | As perguntas do produto são respondidas por consultas OLAP pré-agregadas: resumo por tema, por ano, por tribunal, por órgão, e não por agregação sobre o fato em tempo de request. |
| RNF-08 | A busca full-text é em português, no próprio Postgres, tolerando ausência de acento e erro de digitação. |
