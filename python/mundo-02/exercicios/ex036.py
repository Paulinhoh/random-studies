"""
    Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salario: R$'))
anos_pagamento = int(input('Em quantos anos deseja pagar: '))

qtd_parcelas = anos_pagamento * 12
valor_parcelas = valor_casa / qtd_parcelas
teto_valor_parcelas = salario * 0.30

if valor_parcelas <= teto_valor_parcelas:
    print('Emprestimo Aprovado!!')
    print(f'Valor das parcelas: {valor_parcelas:.2f}')
else:
    print('Emprestimo não aprovado.')
    