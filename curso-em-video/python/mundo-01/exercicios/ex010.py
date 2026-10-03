"""
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
    quantos dolares ela pode comprar.

    Considere US$1.00 == R$3.27
"""

real = float(input('Digite o valor em real: R$'))
dollar = real / 3.27
print(f'Valor em US${dollar:.2f}')
