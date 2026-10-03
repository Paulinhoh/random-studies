"""
    Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint

jogos = []
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(quantidade_jogos):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogos.append(sorted(jogo))

print(f'{"-=" * 3} SORTEANDO {quantidade_jogos} JOGOS {"-=" * 3}')
for i, jogo in enumerate(jogos):
    print(f'Jogo {i + 1}: {jogo}')

