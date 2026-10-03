from abc import ABC, abstractmethod

import math


class Poligono(ABC):

    def __init__(self, qt_lados: int) -> None:
        self.qt_lados = qt_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):

    def __init__(self, lado: float) -> None:
        super().__init__(4)
        self.lado = lado

    def perimetro(self) -> float:
        return self.lado * self.qt_lados

    def area(self) -> float:
        return self.lado ** 2


class Circulo(Poligono):

    def __init__(self, raio: float) -> None:
        super().__init__(0)
        self.raio = raio

    def perimetro(self) -> float:
        return 2 * math.pi * self.raio

    def area(self) -> float:
        return (self.raio ** 2) * math.pi


def main():
    p1 = Quadrado(12)
    print(f'Perimetro: {p1.perimetro():.1f}')
    print(f'Area: {p1.area():.1f}')

    c1 = Circulo(20)
    print(f'Perimetro: {c1.perimetro():.1f}')
    print(f'Area: {c1.area():.1f}')


if __name__ == '__main__':
    main()
