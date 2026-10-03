"""
    Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa.
"""

from rich import print


class Caneta:
    """
    Caneta:
    """

    cores = {
        'vermelha': 'red',
        'verde': 'green',
        'azul': 'blue'
    }

    def __init__(self, cor: str) -> None:
        if cor.lower() in self.__class__.cores.keys():
            self.cor = self.__class__.cores[cor.lower()]
        else:
            self.cor = self.__class__.cores['azul']
        self.tampada = True

    def destampar(self) -> None:
        self.tampada = False

    def tampar(self) -> None:
        self.tampada = True

    def quebrar_linha(self, qtd: int) -> None:
        for i in range(qtd):
            print('')

    def escrever(self, msg: str) -> str:
        if self.tampada:
            return f'A [{self.cor}]caneta[/] está tampada!'

        return f'[{self.cor}]{msg}[/]'


def main():
    c1 = Caneta('azul')
    c2 = Caneta('vermelha')
    c3 = Caneta('verde')

    print(c1.escrever('Olá, mundo!'))
    c1.destampar()
    print(c1.escrever('Olá, mundo!'))

    c2.destampar()
    print(c2.escrever('olá, gafanhoto'))
    c2.quebrar_linha(2)
    print(c2.escrever('bem vindo ao mundo 04'))

    c3.destampar()
    print(c3.escrever('aqui esta em verde'))


if __name__ == '__main__':
    main()
