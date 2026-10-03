"""
    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
n4 = int(input('Digite o 4º valor: '))
n5 = int(input('Digite o 5º valor: '))

numeros = [n1, n2, n3, n4, n5]

print(f'Valores digitados: {numeros}')

print(f'Maior valor: {max(numeros)} na posição {numeros.index(max(numeros))}')

print(f'Menor valor: {min(numeros)} na posição {numeros.index(min(numeros))}')
