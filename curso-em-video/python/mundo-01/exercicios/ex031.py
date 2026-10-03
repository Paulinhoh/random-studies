"""
    Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço
    da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.
"""

dist = float(input('qual a distancia da viagem em km: '))
passagem = 0

if dist <= 200:
    passagem = dist * 0.50
else:
    passagem = dist * 0.45

print(f'valor da passagem: R${passagem:.2f}')
