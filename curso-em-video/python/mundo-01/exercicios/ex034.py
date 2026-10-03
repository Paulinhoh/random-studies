"""
    Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
    Para salarios superiores a R$1.250,00, calcule o aumento em 10%.
    Para os inferiores ou iguais, o aumento e de 15%.
"""

sal = float(input('digite o salario: '))

if sal > 1250:
    print(f'Novo salario com aumento de 10%: {sal+(sal*0.10)}')
else:
    print(f'Novo salario com aumento de 15%: {sal+(sal*0.15)}')
