"""
    Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10
    primeiros termos dessa progressão.
"""

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
casa_ultimo_termo = primeiro_termo + 10 * razao

for i in range(primeiro_termo, casa_ultimo_termo, razao):
    print(i, end=' ')
