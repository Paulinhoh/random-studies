"""
    Fça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
    desse angulo.
"""
import math

angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Seno de {angulo}: {seno}')
print(f'Cosseno de {angulo}: {cosseno}')
print(f'Tangente de {angulo}: {tangente}')