#code smell
#Message Chain o código precisa navegar por vários objetos em sequência
#Violação da Lei de Demeter um objeto conhece detalhes internos demais de outros objetos
#Acoplamento excessivo se mudar alguma classe no meio da cadeia, esse código pode quebrar

class Pais:
    def __init__(self, nome):
        self.nome = nome


class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

    def obter_nome_pais(self):
        return self.pais.nome


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def obter_nome_pais(self):
        return self.estado.obter_nome_pais()


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def obter_nome_pais(self):
        return self.endereco.obter_nome_pais()


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente

    def obter_nome_pais_cliente(self):
        return self.cliente.obter_nome_pais()