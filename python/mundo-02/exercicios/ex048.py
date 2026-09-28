"""
    Faça um programa que calcule a soma de todos os numeros inpares que são multiplos de três e que 
    se encontram no intervalo de 1 até 500.
"""

soma = 0
for i in range(1, 500+1):
    if i % 2 == 1 and i % 3 == 0:
        soma += i

print(f'Soma: {soma}')
