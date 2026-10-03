"""
    Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
"""

metros = float(input('Digite uma medida em metros: '))
centimetros = metros*100
milimetros = metros*1000

print(f'Valor em metros: {metros}m')
print(f'Valor em centimetros: {centimetros}cm')
print(f'Valor em milimetros: {milimetros}mm')
