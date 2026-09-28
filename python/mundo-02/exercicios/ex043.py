"""
    Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu
    IMC e mostre seus status, de acordo com a tabela abaixo:
    - abaixo de 18.5: Abaixo do Peso
    - entre 18.5 e 25: Peso Ideal
    - 25 e 30: Sobrepeso
    - 30 e 40: Obesidade
    - acima de 40: Obesidade mórbida
"""

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)
print(f'IMC: {imc}')

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
