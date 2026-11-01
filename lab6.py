#code smell
#Duplicated Code os métodos de crédito e débito repetem quase a mesma lógica
#Magic Numbers 0.05 e 0.02 aparecem diretamente no cálculo
#Long Method  cada método repete etapas de cálculo e impressão que poderiam ser unificadas

class ProcessadorPagamento:
    TAXA_CREDITO = 0.05
    TAXA_DEBITO = 0.02

    def processar_pagamento(self, valor, tipo):
        if tipo == "CREDITO":
            taxa = self.TAXA_CREDITO

        elif tipo == "DEBITO":
            taxa = self.TAXA_DEBITO

        else:
            raise ValueError("Tipo de pagamento inválido.")

        valor_final = valor + (valor * taxa)

        print(f"Valor final: R$ {valor_final:.2f}")

        return valor_final