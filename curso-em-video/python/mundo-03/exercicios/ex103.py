"""
    Faça um programa que tenha um função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='<desconhecido>', gols=0):
    """
    Mostra a ficha de um jogador.

    :param nome: Nome do jogador (padrão: '<desconhecido>').
    :param gols: Número de gols marcados pelo jogador (padrão: 0).
    :return: None
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Testando a função
nome_jogador = input('Digite o nome do jogador: ')
gols_jogador = input('Digite o número de gols marcados: ')

if gols_jogador.isdigit():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

ficha(nome=nome_jogador, gols=gols_jogador)
