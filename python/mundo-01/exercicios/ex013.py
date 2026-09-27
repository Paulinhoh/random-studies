"""
    Faça um algoritmo que leia o salrio de um funcionario e mostre seu novo
    salario, com 15% de aumento.
"""

salario = float(input('Digite o valor do salario atual: R$'))
new_salario = salario + (salario * 0.15)

print(f'Novo salario com aumento de 15%: R${new_salario:.2f}')
