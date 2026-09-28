"""
    Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se
    o valor for impar desconsidere-o.
"""

soma = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}° numero intero: '))
    if num % 2 == 0:
        soma += num

print(f'Soma dos valores pares: {soma}')
