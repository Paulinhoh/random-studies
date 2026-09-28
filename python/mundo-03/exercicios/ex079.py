"""
    Crie um programa onde o usuario possa digitar cinco valores numéricos e cadastre-os em uma lista, Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista = []

for i in range(5):
    n = int(input(f'Digite o {i+1}º valor: '))
    if n not in lista:
        lista.append(n)

print(f'Valores únicos digitados: {lista}')

lista.sort()
print(f'Valores únicos digitados em ordem crescente: {lista}')
