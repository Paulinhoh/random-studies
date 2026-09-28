"""
    Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade,
    se ela ainda vai se alistar ao serviço militar, se é hora de se alistar ou se ja passou do tempo do
    alistamento. Seu programa também devera mostrar o tempo que falta ou o que passou do prazo.
"""
from datetime import date

year = date.today().year
birthday_year = int(input('Digite o ano de nacimento: '))
age = year - birthday_year

print(f'Idade: {age}')
if age == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - age
    print(
        f'Voce ainda não tem 18 anos. Ainda falta {saldo} anos para o alistamento.')
elif idade > 18:
    saldo = age - 18
    print(f'Voce ja deveria ter se alistado a {saldo} anos.')
