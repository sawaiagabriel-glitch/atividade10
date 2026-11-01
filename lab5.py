# code smell
#Large Class a classe Produto não cuida só dos dados do produto, ela também mexe com banco de dados e exportação
#Inappropriate Intimacy Produto conhece detalhes de SQL e XML
#Magic Number o valor 1.15 aparece diretamente no cálculo de preço
#Feature Envy métodos de persistência e exportação estão dentro da entidade Produto, quando deveriam ficar em classes próprias

class Produto:
    TAXA_AJUSTE = 1.15

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco_ajustado(self):
        return self.preco * self.TAXA_AJUSTE


class ProdutoRepository:
    def salvar(self, produto):
        print(f"Salvando {produto.nome} no banco de dados...")


class ProdutoExporter:
    def exportar_xml(self, produto):
        print(f"Exportando {produto.nome} para XML...")