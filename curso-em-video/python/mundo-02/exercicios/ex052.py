"""
    Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
"""
num = int(input('Digite um numero: '))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} não é um numero primo.')
            break
    else:
        print(f'{num} é um numero primo.')
else:
    print(f'{num} não é um numero primo.')
