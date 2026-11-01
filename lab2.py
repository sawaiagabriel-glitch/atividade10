#Code smell:
# Long Parameter List o construtor de Funcionario recebe parâmetros demais.
#Data Clumps nos dados de endereço e telefone
#código
class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero


class Funcionario:
    def __init__(self, nome, cargo, salario, endereco, telefone):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco
        self.telefone = telefone

    def exibir_dados(self):
        print(f"Funcionário: {self.nome} - {self.cargo}")
        print(f"Contato: ({self.telefone.ddd}) {self.telefone.numero}")
        print(
            f"Endereço: {self.endereco.rua}, {self.endereco.numero} - "
            f"{self.endereco.bairro}, {self.endereco.cidade}/"
            f"{self.endereco.estado} - CEP: {self.endereco.cep}"
        )