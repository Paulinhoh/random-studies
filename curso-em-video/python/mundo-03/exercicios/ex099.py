"""
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(*numeros):
    if len(numeros) == 0:
        print('Nenhum valor foi informado.')
        return None

    maior_valor = numeros[0]
    for num in numeros:
        if num > maior_valor:
            maior_valor = num

    return maior_valor


# Exemplo de uso da função
valores = [int(x) for x in input(
    'Digite os valores separados por espaço: ').split()]
resultado = maior(*valores)
if resultado is not None:
    print(f'O maior valor informado foi: {resultado}')
