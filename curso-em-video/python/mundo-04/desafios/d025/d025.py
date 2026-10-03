from abc import ABC, abstractmethod
from rich import print
from rich.table import Table


class Transporte(ABC):
    def __init__(self, distancia: float) -> None:
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self) -> float:
        pass


class Motor(Transporte):
    fator = 0.50

    def __init__(self, distancia: float) -> None:
        super().__init__(distancia)

    def calc_frete(self) -> float:
        if self.distancia < 0:
            raise ValueError('A distancia não pode ser abaixo de 0.')
        self.frete = self.__class__.fator * self.distancia
        return self.frete


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia: float) -> None:
        super().__init__(distancia)

    def calc_frete(self) -> float:
        if self.distancia < 50:
            raise ValueError('A distância mínima para entregas de caminhão é de 50 km.')
        if self.distancia < 0:
            raise ValueError('A distancia não pode ser abaixo de 0.')
        self.frete = self.__class__.fator * self.distancia
        return self.frete


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia: float) -> None:
        super().__init__(distancia)

    def calc_frete(self) -> float:
        if self.distancia > 10:
            raise ValueError('A distância maxima para entregas de drone é de 10 km.')
        if self.distancia < 0:
            raise ValueError('A distancia não pode ser abaixo de 0.')
        self.frete = self.__class__.fator * self.distancia
        return self.frete


def main():
    dist = 8

    try:
        m1 = Motor(dist)
        print(f'Frete de {type(m1).__name__} em {dist}Km custara R${m1.calc_frete():.2f}')
    except ValueError as e:
        print(f'error: {e}')
    except Exception as e:
        print(f'error: erro desconhecido: {e}')

    print('-' * 20)

    try:
        c1 = Caminhao(dist)
        print(f'Frete de {type(c1).__name__} em {dist}Km custara R${c1.calc_frete():.2f}')
    except ValueError as e:
        print(f'error: {e}')
    except Exception as e:
        print(f'error: erro desconhecido: {e}')

    print('-' * 20)

    try:
        d1 = Drone(dist)
        print(f'Frete de {type(d1).__name__} em {dist}Km custara R${d1.calc_frete():.2f}')
    except ValueError as e:
        print(f'error: {e}')
    except Exception as e:
        print(f'error: erro desconhecido: {e}')


if __name__ == '__main__':
    main()
