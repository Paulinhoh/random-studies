"""
    Faça um programa qe leia o nome completo de uma pessoa, mostrando
    em seguida o primeiro e o ultimo nome separadamente.
"""

name = str(input('Digite seu nome completo: ')).strip()
names = name.split()

print(f'Primeiro nome: {names[0]}')
print(f'Ultimo nome: {names[-1]}')
