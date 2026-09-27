"""
    Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem 
    ou não formar um triangulo.
"""

a = int(input('digite a 1° reta: '))
b = int(input('digite a 2° reta: '))
c = int(input('digite a 3° reta: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('Podem formar um triangulo!')
else:
    print('Não podem formar um triangulo!')
