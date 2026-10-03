"""
    Melhore o jogo do desafio 028 onde o computador "pensa" em um numero entre 0 e 10. Só que agora
    o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios
    para vencer.
"""

import random

computador = random.randint(0, 10)
tentativas = 0
acertou = False

while acertou == False:
    escolha = int(input('Digite o valor entre 0 e 10: '))
    tentativas += 1

    if escolha == computador:
        print('Parabéns! Voce acertou o numero exato.')
        print(f'Quantidades de tentativas: {tentativas}')
        acertou = True
    else:
        print('Sinto muito, resposta errada!')
        print('Tente novamente!')
