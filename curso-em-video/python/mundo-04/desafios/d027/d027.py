from abc import ABC, abstractmethod
import random
from rich import print


class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = 100
        self.golpes = []

    def atacar(self, alvo: Personagem, forca=80):
        if self.vida > 0 and alvo.vida > 0:
            golpe = random.choice(self.golpes)
            print(f'[green]{self.nome}[/]({self.vida}) atacaou [red]{alvo.nome}[/]({alvo.vida}) com [blue]{golpe}[/]')
            alvo.receber_dano(forca)
        else:
            print(f'[red]O ataque de {self.nome} -> {alvo.nome} não pode acontecer[/]')

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida <= 0:
            self.vida = 0
        print(f'[blue]{self.nome}[/] recebeu [red]{fator} de dano[/]!')

    def staus(self):
        print('-' * 20)
        print(f'Personagem: {self.nome}\nVida: {self.vida}')
        print('-' * 20)

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['soco', 'Golpe de Machado', 'Pulo Giratório']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[green]{self.nome} enrolou uma atadura nos ferimentos e recuperou {fator} de vida[/]')


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Raio de Luz', 'Magia Estatica']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[green]{self.nome} fez uma magia de cura e recuperou {fator} de vida[/]')


def main():
    p1 = Guerreiro('Kratos', 100)
    p2 = Mago('Gandalf', 100)

    p1.atacar(p2, 100)
    p2.curar()
    p2.atacar(p1, 100)
    p2.atacar(p1, 100)

    p1.staus()
    p2.staus()


if __name__ == '__main__':
    main()
