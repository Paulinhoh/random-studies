"""
    Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
    a) Quantos numeros foram digitados.
    b) A lista de valores ordenada em ordem decrescente.
    c) Se o valor 5 foi digitado e esta ou nao na lista.
"""

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

print(f'Quantidade de números digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista de valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
