"""
    Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
"""

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

if (n1 > n2) and (n1 > n3):
    print(f'O maio é {n1}')
elif (n2 > n1) and (n2 > n3):
    print(f'O maio é {n2}')
else:
    print(f'O maio é {n3}')
