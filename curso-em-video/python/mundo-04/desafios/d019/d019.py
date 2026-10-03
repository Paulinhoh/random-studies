"""
    Crie a classe Livro que vai simular a passagem de paginas de um livro, considerando também
    se o usuario chegou ao fim da leitura.
"""

from rich import print


class Livro:
    """
    Livro:
    """

    def __init__(self, titulo: str, paginas: int) -> None:
        self.titulo = titulo
        self.paginas = paginas
        self.paginas_lidas = 1

        print(
            f"[blue]:book: Você acabou de abrir o livro[/] [red]'{self.titulo}'[/] [blue]que tem[/] [green]{self.paginas} páginas[/] [blue]no total. Você agora está na[/] [yellow]página {self.paginas_lidas}[/]")

    def avancar_paginas(self, qtd_paginas: int) -> None:
        count = 0

        if self.paginas_lidas >= self.paginas:
            print(f"[red]:book: Você chegou ao final do livro '{self.titulo}'[/]")
            return

        for page in range(qtd_paginas):
            if self.paginas_lidas >= self.paginas:
                print(f'[blue]Voce avançou {count} páginas e agora esta na[/] [yellow]página {self.paginas_lidas}[/]')
                print(f"[red]:book: Você chegou ao final do livro '{self.titulo}'[/]")
                return

            self.paginas_lidas += 1
            print(f'Pág{self.paginas_lidas}', end=' -> ')
            count += 1

        print(f'[blue]Voce avançou {count} páginas e agora esta na[/] [yellow]página {self.paginas_lidas}[/]')


def main():
    l1 = Livro('10 coisas que aprendi', 20)
    l1.avancar_paginas(5)
    l1.avancar_paginas(10)
    l1.avancar_paginas(50)


if __name__ == '__main__':
    main()
