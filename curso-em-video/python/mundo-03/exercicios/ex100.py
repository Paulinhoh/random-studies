"""
    Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

import random

numeros = []


def sorteia():
    for _ in range(5):
        numeros.append(random.randint(1, 10))


def somaPar():
    return sum(x for x in numeros if x % 2 == 0)


# Chamando as funções
sorteia()

print(f'Números sorteados: {numeros}')
print(f'Soma dos pares: {somaPar()}')
