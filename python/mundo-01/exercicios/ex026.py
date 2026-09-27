"""
    Faça um programa que leia uma frase pelo teclado e mostre:
    - quantas vezes aparece a letra 'A'
    - em que posição ela aparece a primeira vez
    - em que posição ele aparece a ultima vez
"""

frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "A" apareceu {frase.count("a")} vezes')
print(f'Aparece pela primeira vez: {frase.find('a')+1}')
print(f'Aparece pela ultima vez: {frase.rfind('a')+1}')
