"""
    Faça um programa que leia um numero de 0 a 9_999 e mostre na tela cada um dos
    digitos separadamente.

    Ex.: 1834 -> unidade:4 dezena:3 centena:8 milhar:1
"""
from ast import parse

num = int(input('Digite um numero entre 0 e 9999: '))
num = str(num)
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')
