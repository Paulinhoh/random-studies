"""
    Elabora um programa que calcule o valor a ser pago por um produto, considerando
    o seu preço normal e condição de pagamento;
    - a vista dinheiro/cheque: 10% de desconto
    - a vista no cartão: 5% de desconto
    - em até x2 no cartão: preço normal
    - 3x ou mains no cartão: 20% de juros
"""


valor_produto = float(input('Digite o valor do produto: R$ '))
print('''Escolha a forma de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma_pagamento = int(input('-> '))

variacao = 0
if forma_pagamento == 1:
    variacao = valor_produto * 0.10
    print(f'Valor final: {valor_produto-variacao}')
elif forma_pagamento == 2:
    variacao = valor_produto * 0.05
    print(f'Valor final: {valor_produto-variacao}')
elif forma_pagamento == 3:
    variacao = valor_produto * 0
    print(f'Valor final: {valor_produto-variacao}')
elif forma_pagamento == 4:
    variacao = valor_produto * 0.20
    print(f'Valor final: {valor_produto+variacao}')
else:
    print('Opção Invalida! Tente novamente.')
