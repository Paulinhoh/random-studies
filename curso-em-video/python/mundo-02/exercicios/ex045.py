"""
    Crie um programa que faça o computador jogar jokenpô com voce.
"""

from random import choice

opcoes_jokenpo = ['pedra', 'papel', 'tesoura']
computador_escolha = choice(opcoes_jokenpo)

print("""Pedra, Papel e Tesora:
[1] Pedra
[2] Papel
[3] Tesoura""")
jogador_escolha = int(input('-> '))

if (jogador_escolha == 1 and computador_escolha == 'tesoura') or (jogador_escolha == 2 and computador_escolha == 'pedra') or (jogador_escolha == 3 and computador_escolha == 'papel'):
    print(f'Computador escolheu: {computador_escolha}')
    print('Jogador venceu.')
elif (jogador_escolha == 1 and computador_escolha == 'papel') or (jogador_escolha == 2 and computador_escolha == 'tesoura') or (jogador_escolha == 3 and computador_escolha == 'pedra'):
    print(f'Computador escolheu: {computador_escolha}')
    print('Computador venceu.')
elif (jogador_escolha == 1 and computador_escolha == 'pedra') or (jogador_escolha == 2 and computador_escolha == 'papel') or (jogador_escolha == 3 and computador_escolha == 'tesoura'):
    print(f'Computador escolheu: {computador_escolha}')
    print('Empate')
else:
    print('Opção Invalida! Tente novamente.')
