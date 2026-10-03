"""
    Escreva um programa que faça computador "pensar" em um numero inteiro entre 0 e 5 e peça para
    o usuario tentar descobrir qual foi o numero escolhido pelo computador.
    O programa devera escrever na tela se o usuario venceu ou perdeu. 
"""

import random

computador = random.randint(0, 5)
escolha = int(input('Digite o valor entre 0 e 5: '))

if escolha == computador:
    print('Parabéns! Voce acertou o numero exato.')
else:
    print('Sinto muito, resposta errada!')
    print(f'Numero correto: {computador}')
