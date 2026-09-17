# Definition of Ready (DoR)

Um único checklist para o time, aplicado a **todo item do Product Backlog antes de entrar em
uma Sprint**. Ele responde a uma pergunta: *este item está pronto para ser construído?*

Uma história só entra na Sprint quando os itens abaixo estão atendidos.

1. **Regras de negócio detalhadas** — o que o item faz, seus limites e o que acontece nos caminhos de exceção.
2. **Dados a armazenar definidos** — campos, tipos, se são obrigatórios e validações; quando o item toca o Data Warehouse, o **grão da tabela fato é declarado por escrito**.
3. **Mensagens de confirmação, erro e alerta definidas** — o texto exato de cada uma.
4. **Protótipo de tela** — wireframe aprovado ou tela navegável, quando o item tem interface.
5. **Critérios de aceite escritos em BDD** — ao menos um cenário por regra relevante, incluindo o caminho de exceção.
6. **Procedência declarada** — para todo número que o item exibe, está definido de onde vem a fonte.
7. **Fonte verificada**, quando o item depende de uma fonte ainda não confirmada — a investigação acontece no refinamento e a resposta é registrada por escrito. Sem isso o item não é comprometido.