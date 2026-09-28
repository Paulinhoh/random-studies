"""
    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
"""

maior_peso = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    if peso > maior_peso:
        maior_peso = peso

print(f'Maio peso: {maior_peso}')
