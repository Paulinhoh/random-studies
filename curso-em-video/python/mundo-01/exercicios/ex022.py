"""
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    - o nome com todas as letras maiusculas e minusculas
    - quantos letras tem ao todo (sem considerar os espaços)
    - quantos letras tem o primeiro nome
"""

name = input('Digite seu nome: ')

print(f'Maiusculas: {name.upper()}')
print(f'Minusculas: {name.lower()}')
print(f'Total de letras no nome: {len(name.replace(' ', ''))}')

names = name.split()
print(f'Quantidade de letras no primeiro nome: {len(names[0])}')
