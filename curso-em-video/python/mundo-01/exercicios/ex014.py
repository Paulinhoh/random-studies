"""
    Escreva um programa que converta uma temperatura digitada em °C e converta
    para °F.
"""

c = float(input('Temperatura em C: '))
f = ((c*9)/5)+32

print(f'Temperatura em Fahrenheit: {f:.1f}°F.')