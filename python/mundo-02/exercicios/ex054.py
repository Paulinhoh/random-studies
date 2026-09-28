"""
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
    atigiram a maioridade e quantas ja são de maiores.
"""
from datetime import date

ano_atual = date.today().year
soma_maioridade = 0
soma_nao_maioridade = 0

for i in range(1, 8):
    ano_nasc = int(input(f'Digite o ano de nacimento da {i}° pessoa: '))
    if ano_atual - ano_nasc >= 21:
        soma_maioridade += 1
    else:
        soma_nao_maioridade += 1

print(f'Quantidade de pessoas Maiores de idade: {soma_maioridade}')
print(f'Quantidade de pessoas Menores de idade: {soma_nao_maioridade}')
