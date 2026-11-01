#Os principais code smells presentes são
#Long Method um único método faz cálculo, desconto, pagamento e relatório
#Large Class GerenciadorDeVendas concentra responsabilidades diferentes
#Magic Number o valor 0.90 está fixo diretamente no código


#código correto:
class CalculadoraVenda:
    DESCONTO_VIP = 0.10

    def calcular_total(self, itens, cliente):
        total = sum(
            item["preco"] * item["quantidade"]
            for item in itens
        )

        if cliente["tipo"] == "VIP":
            total *= (1 - self.DESCONTO_VIP)

        return total


class ProcessadorPagamento:
    def processar(self, metodo_pagamento, total):
        if metodo_pagamento == "CARTAO":
            print(f"Cobrando R$ {total:.2f} no cartão de crédito...")

        elif metodo_pagamento == "BOLETO":
            print(f"Gerando boleto no valor de R$ {total:.2f}...")


class GeradorRelatorio:
    def gerar(self, cliente, total):
        relatorio = (
            "--- Relatório de Venda ---\n"
            f"Cliente: {cliente['nome']}\n"
            f"Total: R$ {total:.2f}\n"
        )

        with open("relatorio_vendas.txt", "a") as arquivo:
            arquivo.write(relatorio)


class GerenciadorDeVendas:
    def __init__(self):
        self.calculadora = CalculadoraVenda()
        self.pagamento = ProcessadorPagamento()
        self.relatorio = GeradorRelatorio()

    def processar_venda(self, itens, cliente, metodo_pagamento):
        total = self.calculadora.calcular_total(itens, cliente)

        self.pagamento.processar(
            metodo_pagamento,
            total
        )

        self.relatorio.gerar(
            cliente,
            total
        )

        print("Venda processada com sucesso.")
