"""
    Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteudo das tres listas geradas.
"""

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

pares = [x for x in lista if x % 2 == 0]
impares = [x for x in lista if x % 2 != 0]

print(f'Lista completa: {lista}')
print(f'Lista de valores pares: {pares}')
print(f'Lista de valores ímpares: {impares}')
