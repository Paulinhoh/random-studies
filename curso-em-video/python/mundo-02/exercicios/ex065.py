"""
    Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média
    entre todos os valores e qual foi o maio e o menor valores lidos. O programa deve perguntar ao usuario
    se ele quer ou não continuar a digitar valores.
"""

soma = 0
qt_elementos = 0
maior_valor = 0
menor_valor = 1_000_000_000

continuar = True
while continuar:
    valores = int(input('Digite um valor: '))

    if valores > maior_valor:
        maior_valor = valores

    if valores < menor_valor:
        menor_valor = valores

    soma += valores
    qt_elementos += 1

    resp = str(input('Continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        continuar = False


print(f'Quantidade de numeros digitados: {qt_elementos}')
print(f'Soma dos elementos: {soma}')
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')
