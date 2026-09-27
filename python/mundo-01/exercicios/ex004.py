"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
    sobre ele.
"""

entrada = str(input("Digite algo: "))
print(f'Tipo primitivo: {type(entrada)}')
print(f'Só tem espaços? {entrada.isspace()}')
print(f'É um numero? {entrada.isnumeric()}')
print(f'É alfabeto? {entrada.isalpha()}')
print(f'É alfanumerico? {entrada.isalnum()}')
print(f'Esta em maiuscula? {entrada.isupper()}')
print(f'Esta em minuscula? {entrada.islower()}')
print(f'Esta capitalizada? {entrada.istitle()}')
