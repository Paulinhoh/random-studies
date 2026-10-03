from abc import ABC, abstractmethod


class BebidaQuenter(ABC):

    def __init__(self) -> None:
        pass

    def preparar(self):
        print('-- Iniciando o preparo --')
        self.fever_agua()
        self.mistura()
        self.servir()
        print('-- Bebida Pronta')

    def fever_agua(self):
        print('1. Fervendo agua a 100 °C;')

    @abstractmethod
    def mistura(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuenter):

    def __init__(self) -> None:
        super().__init__()

    def mistura(self):
        print('2. Passando água pressurizada pelo pó de café moído;')

    def servir(self):
        print('3. Servindo em chicara pequena;')


class Cha(BebidaQuenter):

    def __init__(self) -> None:
        super().__init__()

    def mistura(self):
        print('2. Mergulhando o sachê de ervas na água;')

    def servir(self):
        print('3. Servindo na caneca de porcelana com limão;')


class Leite(BebidaQuenter):

    def __init__(self) -> None:
        super().__init__()

    def mistura(self):
        print('2. Passando vapor pressurizada pelo bico do leite;')

    def servir(self):
        print('3. Servindo na caneca grande já com café;')


def main():
    b1 = Cafe()
    b1.preparar()
    print('-' * 20)
    b2 = Cha()
    b2.preparar()
    print('-' * 20)
    b3 = Leite()
    b3.preparar()


if __name__ == '__main__':
    main()
