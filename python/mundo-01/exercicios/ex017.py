"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
    de um triangulo retangulo, calcule e o valor da hipotenusa.
"""
import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

# h² = co² + ca²
hipotenusa = math.hypot(co, ca)

print(f'Hipotenusa: {hipotenusa:.2f}')
