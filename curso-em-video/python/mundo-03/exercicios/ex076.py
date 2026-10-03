"""
    Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

produtos = ('Arroz', 5.50, 'Feijão', 7.30, 'Macarrão', 3.20, 'Açúcar', 4.10, 'Óleo', 6.00)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<30} R$ {produtos[i + 1]:>7.2f}')
