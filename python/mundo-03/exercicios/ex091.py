"""
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep

jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}

for jogador, valor in jogadores.items():
    print(f'{jogador} tirou {valor} no dado.')
    sleep(1)

print('\nRanking dos jogadores:')
for i, (jogador, valor) in enumerate(sorted(jogadores.items(), key=lambda x: x[1], reverse=True), start=1):
    print(f'{i}º lugar: {jogador} com {valor} pontos')
