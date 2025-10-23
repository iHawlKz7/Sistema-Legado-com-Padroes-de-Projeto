from abc import ABC, abstractmethod

# Padrão Strategy
class EstrategiaPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class PagamentoPix(EstrategiaPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando R${valoracao:.2f} via PIX...")
        return True

class PagamentoCredito(EstrategiaPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando R${valor:.2f} via Cartão de Crédito...")
        return True

class PagamentoMana(EstrategiaPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando R${valor:.2f} via Transferência de Mana...")
        return True

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular_frete(self, valor):
        pass

class FreteNormal(EstrategiaFrete):
    def calcular_frete(self, valor):
        custo_frete = valor * 0.05
        print(f"Frete Normal: R${custo_frete:.2f}")
        return custo_frete

class FreteExpresso(EstrategiaFrete):
    def calcular_frete(self, valor):
        custo_frete = valor * 0.10 + 15.00
        print(f"Frete Expresso (com taxa): R${custo_frete:.2f}")
        return custo_frete

class FreteTeletransporte(EstrategiaFrete):
    def calcular_frete(self, valor):
        custo_frete = 50.00
        print(f"Frete Teletransporte: R${custo_frete:.2f}")
        return custo_frete

# Classe monolítica com Strategy
class SistemaPedidoAntigo:
    def _init_(self, itens, estrategia_pagamento, estrategia_frete, tem_embalagem_presente=False):
        self.itens = itens
        self.estrategia_pagamento = estrategia_pagamento
        self.estrategia_frete = estrategia_frete
        self.valor_base = sum(item['valor'] for item in itens)
        self.tem_embalagem_presente = tem_embalagem_presente

    def aplicar_desconto(self):
        if self.estrategia_pagamento._class.name_ == 'PagamentoPix':
            print("Aplicando 5% de desconto PIX.")
            return self.valor_base * 0.95
        elif self.valor_base > 500:
            print("Aplicando 10% de desconto para pedidos grandes.")
            return self.valor_base * 0.90
        else:
            return self.valor_base

    def calcular_frete(self, valor_com_desconto):
        return self.estrategia_frete.calcular_frete(valor_com_desconto)

    def processar_pagamento(self, valor_final):
        return self.estrategia_pagamento.processar_pagamento(valor_final)

    def finalizar_compra(self):
        print("=========================================")
        print("INICIANDO CHECKOUT...")
        valor_apos_desconto = self.aplicar_desconto()
        custo_frete = self.calcular_frete(valor_apos_desconto)
        valor_final = valor_apos_desconto + custo_frete
        if self.tem_embalagem_presente:
            taxa = 5.00
            valor_final += taxa
            print(f"Adicionando R${taxa:.2f} de Embalagem de Presente.")
        print(f"\nValor a Pagar: R${valor_final:.2f}")
        if self.processar_pagamento(valor_final):
            print("\nSUCESSO: Pedido finalizado e registrado no estoque.")
            print("Emitindo nota fiscal (lógica de subsistema oculta).")
            return True
        else:
            print("\nFALHA: Transação abortada.")
            return False

# USO ATUAL (CENÁRIOS DE TESTE)
if _name_ == "_main_":
    # Cenário 1: Pedido com PIX (Desconto) e Frete Normal.
    itens_p1 = [{'nome': 'Capa da Invisibilidade', 'valor': 150.0}, {'nome': 'Poção de Voo', 'valor': 80.0}]
    pedido1 = SistemaPedidoAntigo(itens_p1, PagamentoPix(), FreteNormal())
    pedido1.finalizar_compra()

    print("\n--- Próximo Pedido ---")

    # Cenário 2: Pedido Grande (Desconto) com Cartão (Lógica de limite) e Embalagem Presente (Lógica de taxa).
    itens_p2 = [{'nome': 'Cristal Mágico', 'valor': 600.0}]
    pedido2 = SistemaPedidoAntigo(itens_p2, PagamentoCredito(), FreteExpresso(), tem_embalagem_presente=True)
    pedido2.finalizar_compra()