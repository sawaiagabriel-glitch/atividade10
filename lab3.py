# code smell:
# Long Parameter List
# Data Clumps
# Magic Number no 50 do café da manhã

class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Quarto:
    def __init__(self, numero, tipo, valor_diaria):
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = valor_diaria


class Reserva:
    TAXA_CAFE = 50

    def __init__(self, hospede, quarto, data_checkin, data_checkout, possui_cafe_da_manha):
        self.hospede = hospede
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.possui_cafe_da_manha = possui_cafe_da_manha

    def calcular_total(self):
        total_dias = (self.data_checkout - self.data_checkin).days
        total = total_dias * self.quarto.valor_diaria

        if self.possui_cafe_da_manha:
            total += self.TAXA_CAFE * total_dias

        return total

    def exibir_reserva(self):
        print(f"Reserva criada para {self.hospede.nome} (CPF: {self.hospede.cpf})")
        print(f"Quarto {self.quarto.numero} ({self.quarto.tipo})")
        print(f"De {self.data_checkin} até {self.data_checkout}")
        print(f"Total a pagar: R$ {self.calcular_total()}")