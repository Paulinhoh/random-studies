"""
    Crie a classe Churrasco, onde seja possivel informar quantas pessoas vão participar e mostre quanto
    de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
"""

from rich import print
from rich.panel import Panel


class Churrasco:
    """
    Churrasco:
    """

    consumo_padrao: float = 0.400
    preco_kg: float = 82.40

    def __init__(self, titulo: str, quant: int) -> None:
        self.titulo = titulo
        self.participantes = quant

    def analisar(self) -> Panel:
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]\nCada participante comerá {self.__class__.consumo_padrao:.1f}Kg e cada Kg custa R${self.__class__.preco_kg:,.2f}\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]\nCada pessoa pagará [yellow]R${self.calcular_custo_por_pessoa():,.2f}[/] para participar.'
        panel = Panel(conteudo, title=self.titulo)
        return panel

    def calcular_qtd_carne(self) -> float:
        qtd_carne = self.participantes * self.__class__.consumo_padrao
        return qtd_carne

    def calcular_custo_total(self) -> float:
        total = self.calcular_qtd_carne() * self.__class__.preco_kg
        return total

    def calcular_custo_por_pessoa(self) -> float:
        total_pessoa = self.calcular_custo_total() / self.participantes
        return total_pessoa


def main():
    c1 = Churrasco('Churras dos Amigos', 15)
    print(c1.analisar())


if __name__ == '__main__':
    main()
