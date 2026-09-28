"""
    Faça um programa que leia um numero qualquer e mostre o seu farorial.
    Ex.: 5! = 5x4x3x2x1=120
"""

num = int(input('Digite um valor: '))
fatorial = 1

print(f'{num}! = ', end='')
while num > 0:
    fatorial *= num
    if num > 1:
        print(f'{num}', end='x')
    else:
        print(f'{num}', end=' = ')
    num -= 1

print(fatorial)
