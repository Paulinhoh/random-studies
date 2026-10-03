"""
    Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

name = str(input('Informe o nome de uma pessoa: ')).strip().lower()
print('silva' in name)
