"""
    Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos
    de uma sequencia de fibonacci.

    Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

n = int(input('Digite o valor de n: '))

e1 = 0
e2 = 1

while n > 0:
    if n > 1:
        print(f'{e1}', end=' -> ')
    else:
        print(f'{e1}')

    temp = e1 + e2
    e1 = e2
    e2 = temp
    n -= 1
