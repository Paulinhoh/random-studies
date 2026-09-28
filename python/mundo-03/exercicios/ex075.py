"""
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
"""

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))

tupla = (num1, num2, num3, num4)

print(f'Os valores digitados foram: {tupla}')

# A) Quantas vezes apareceu o valor 9.
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')

# B) Em que posição foi digitado o primeiro valor 3.
if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na posição {tupla.index(3)}')
else:
    print('O valor 3 não foi digitado.')

# C) Quais foram os números pares.
pares = [x for x in tupla if x % 2 == 0]
print(f'Os números pares são: {pares}')
