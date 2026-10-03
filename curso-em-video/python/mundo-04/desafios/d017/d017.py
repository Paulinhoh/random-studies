"""
    Crie a classe produto, onde podemos cadastrar nome e preço. Crie também um método que mostre
    uma etiqueta de preço do produto.
"""

from rich import print
from rich.panel import Panel


class Produto:
    """
    Produto:
    """

    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def etiqueta(self) -> Panel:
        conteudo = f'{self.nome:^36}\n{'-' * 36}\n{f'R${self.preco:,.2f}':.^36}'
        etiqueta = Panel(conteudo, title='Produto', width=40)
        return etiqueta


def main():
    p1 = Produto('iPhone 17 Pro Max', 25_000.85)
    p2 = Produto('Notebook Gamer', 8_720)

    print(p1.etiqueta())
    print(p2.etiqueta())


if __name__ == "__main__":
    main()
