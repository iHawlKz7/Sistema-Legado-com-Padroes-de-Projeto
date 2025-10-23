# Sistema-Legado-com-Padroes-de-Projeto
tf
Arquitetura utiliza o padrão Strategy para tornar flexíveis as estratégias de pagamento e frete, permitindo que sejam trocadas facilmente sem alterar a lógica da classe "sistemapedidoantigo"

Objetivo: Tornar flexíveis as estratégias de pagamento e frete.
Implementação: Interfaces abstratas EstrategiaPagamento e EstrategiaFrete com classes concretas para cada método de pagamento e tipo de frete.