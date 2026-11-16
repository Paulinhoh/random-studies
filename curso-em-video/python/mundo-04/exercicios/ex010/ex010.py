from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome: str = ''):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f'{self.nome} é {self.__class__.__name__} e esta emitindo um som')


class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'QUACK! QUACK!'")


class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'AU! AU! AU!'")


class Spitz(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'au! au! au! au! au!'")


class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'RUFF! RUFF!'")


class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'MIAU! MIAU!'")


class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'PO! PO! PO!'")


def main():
    a = Cachorro('Bandit')
    b = Gato('Frajola')
    c = Pato('Donald')
    d = Spitz('Luluzinha')
    e = Pitbull('Hulk')

    a.emitir_som()
    b.emitir_som()
    c.emitir_som()
    d.emitir_som()
    e.emitir_som()


if __name__ == '__main__':
    main()
