from abc import ABC, abstractmethod

# Strategy
class EstrategiaPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class PagamentoPix(EstrategiaPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando R${valor:.2f} via PIX...")
        return True

class PagamentoCredito(EstrategiaPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando R${valor:.2f} via Cartão de Crédito...")
        return True

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular_frete(self, valor):
        pass

class FreteNormal(EstrategiaFrete):
    def calcular_frete(self, valor):
        return valor * 0.05

# Decorator
class PedidoDecorator(ABC):
    def _init_(self, pedido):
        self.pedido = pedido

    def calcular_valor(self):
        return self.pedido.calcular_valor()

class DescontoPix(PedidoDecorator):
    def calcular_valor(self):
        valor = self.pedido.calcular_valor()
        return valor * 0.95

class TaxaEmbalagemPresente(PedidoDecorator):
    def calcular_valor(self):
        valor = self.pedido.calcular_valor()
        return valor + 5.00

# Facade
class CheckoutFacade:
    def _init_(self, pedido):
        self.pedido = pedido

    def concluir_transacao(self):
        valor = self.pedido.calcular_valor()
        # Processar pagamento e frete
        return True

class Pedido:
    def _init_(self, valor, estrategia_pagamento, estrategia_frete):
        self.valor = valor
        self.estrategia_pagamento = estrategia_pagamento
        self.estrategia_frete = estrategia_frete

    def calcular_valor(self):
        return self.valor + self.estrategia_frete.calcular_frete(self.valor)

    def processar_pagamento(self):
        return self.estrategia_pagamento.processar_pagamento(self.calcular_valor())

# Uso
pedido = Pedido(100.00, PagamentoPix(), FreteNormal())
pedido = DescontoPix(pedido)
pedido = TaxaEmbalagemPresente(pedido)
checkout = CheckoutFacade(pedido)
checkout.concluir_transacao()