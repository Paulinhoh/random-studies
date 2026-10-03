"""
    Faça um programa que leia o nome de uma cidade e diga se ela começa ou não
    com o nome "Santo".
"""

city = str(input('Informe o nome da cidade: ')).strip().lower()
print('santo' in city[:5])
