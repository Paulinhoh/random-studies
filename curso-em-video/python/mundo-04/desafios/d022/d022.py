"""
    Crie uma classe ControleRemoto, onde vamos simular o funcionamento de um controle simples
    (canal, volume e ligar/desligar)
"""

from rich import print
from rich.panel import Panel
import os


class ControleRemoto:
    """
    ControleRemoto:
    """

    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal: int = 1, volume: int = 2) -> None:
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False

    def get_canal(self) -> int:
        return self.canal_atual

    def get_volume(self) -> int:
        return self.volume_atual

    def liga_desliga(self) -> None:
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == self.__class__.canal_max:
                self.canal_atual = self.__class__.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == self.__class__.canal_min:
                self.canal_atual = self.__class__.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != self.__class__.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != self.__class__.volume_min:
                self.volume_atual -= 1

    def mostrar_tv(self) -> Panel:
        if not self.ligado:
            conteudo = f'[red]:prohibited: A TV está desligada[/]'
        else:
            conteudo = f'CANAL = '
            for canal in range(self.__class__.canal_min, self.__class__.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f'[yellow on yellow] {canal} [/]'
                else:
                    conteudo += f' {canal} '

            conteudo += '\nVOLUME = '
            for volume in range(self.__class__.volume_min, self.__class__.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f'[black on cyan] [/]'
                else:
                    conteudo += f'[black on white] [/]'

        tv = Panel(conteudo, title='[ TV ]', width=40)
        return tv


def main():
    c = ControleRemoto()

    while True:
        print(c.mostrar_tv())
        comando = str(input(f' < CH{c.get_canal()} >   - VOL{c.get_volume()}: +  '))

        match comando:
            case '0':
                break
            case '@':
                c.liga_desliga()
            case '<':
                c.canal_menos()
            case '>':
                c.canal_mais()
            case '+':
                c.volume_mais()
            case '-':
                c.volume_menos()
        print(os.system('cls'))


if __name__ == '__main__':
    main()
