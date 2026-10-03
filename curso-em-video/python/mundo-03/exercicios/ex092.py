"""
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime

pessoa = {}
pessoa['nome'] = input('Digite o nome da pessoa: ')
pessoa['nascimento'] = int(input('Digite o ano de nascimento: '))
pessoa['idade'] = datetime.now().year - pessoa['nascimento']
pessoa['ctps'] = int(
    input('Digite o número da carteira de trabalho (0 se não tiver): '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite o salário: '))
    pessoa['aposentadoria'] = pessoa['contratacao'] + 35 - datetime.now().year

print(pessoa)
