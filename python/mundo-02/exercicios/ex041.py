"""
    A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
    e mostre sua categoria de acordo com a idade.
"""

from datetime import date

year = date.today().year
birthday_year = int(input('Digite o ano de nascimento: '))
age = year - birthday_year

if age < 10:
    print('MIRIM')
elif age >= 10 and age < 15:
    print('INFANTIL')
elif age >= 15 and age < 20:
    print('JUNIOR')
elif age >= 20 and age < 26:
    print("SENIOR")
else:
    print('MASTER')
