from functools import singledispatchmethod


class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print(f'Não foi possivel analisar o valor {valor}')

    @analisar.register
    def _(self, valor: int):
        print(f'{valor} é um numero inteiro')

    @analisar.register
    def _(self, valor: float):
        print(f'{valor} é um numero real')

    @analisar.register
    def _(self, valor: str):
        print(f'{valor} é uma cadeia de caracteres')

    @analisar.register
    def _(self, valor: tuple | list | dict):
        print(f'{valor} é uma coleção de dados')

    @analisar.register
    def _(self, valor: bool):
        print(f'{valor} é um valor boolean')


def main():
    x = Analisador()
    x.analisar('Oi')
    x.analisar(72)
    x.analisar(8.5)
    x.analisar({"idade": 21})
    x.analisar(True)


if __name__ == '__main__':
    main()
