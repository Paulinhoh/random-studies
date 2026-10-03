"""
    Crie uma classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um método
    que permita mostrar a ficha desse gamer.
"""
from difflib import context_diff

from rich import print
from rich.panel import Panel


class Gamer:
    """
    Gamer:
    """

    def __init__(self, nome: str, nick: str) -> None:
        self.nome = nome
        self.nick = nick
        self.lista_jogos = list()

    def add_favoritos(self, game: str) -> None:
        self.lista_jogos.append(game)
        self.ordenar_jogos()

    def ordenar_jogos(self) -> None:
        self.lista_jogos.sort()

    def mostrar_jogos(self) -> str:
        conteudo = ''
        for jogo in self.lista_jogos:
            conteudo += f':video_game: {jogo}\n'
        return conteudo

    def ficha(self) -> Panel:
        conteudo = f'Nome real: {self.nome}\nJogos favoritos:\n{self.mostrar_jogos()}'
        ficha = Panel(conteudo, title=f'Jogador <{self.nick}>', width=40)
        return ficha


def main():
    j1 = Gamer('Paulo Henrique', 'paulinoh')
    j1.add_favoritos('Zelda: Breath of the wild')
    print(j1.ficha())

    j2 = Gamer('Olivia Souza', 'peach_raivosa')
    j2.add_favoritos('Mario Bros')
    j2.add_favoritos('Call of Dutty')
    j2.add_favoritos('God of War')
    print(j2.ficha())


if __name__ == '__main__':
    main()
