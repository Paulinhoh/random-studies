"""
    Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
"""

lista = []
while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    lista.append([nome, peso])
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(lista)} pessoas.')

if lista:
    maior_peso = max(lista, key=lambda x: x[1])[1]
    menor_peso = min(lista, key=lambda x: x[1])[1]

    print(f'O maior peso é {maior_peso} kg.')
    print(f'O menor peso é {menor_peso} kg.')

    print('Pessoas mais pesadas:')
    for pessoa in lista:
        if pessoa[1] == maior_peso:
            print(f'{pessoa[0]} - {pessoa[1]} kg')

    print('Pessoas mais leves:')
    for pessoa in lista:
        if pessoa[1] == menor_peso:
            print(f'{pessoa[0]} - {pessoa[1]} kg')
