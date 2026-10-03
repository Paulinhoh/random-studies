"""
    Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela
    uma mensagem:
    - O primeiro é maior
    - O segundo é maior
    - Não existe valor maior, os dois são iguais
"""

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('O primeiro é maior')
elif n2 > n1:
    print('O segundo é maior')
else:
    print('Não existe valor maior, os dois são iguais')
