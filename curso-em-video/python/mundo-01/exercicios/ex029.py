"""
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80km/h, mostra uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada km acima do limite.
"""

velo = int(input('qual a velocidade do carro em km: '))

if velo > 80:
    print('acima da velocidade... voce sera multado')
    multa:float = (velo - 80) * 7
    print(f'valor da multa: {multa:.2f}')
else:
    print('dentro do limite de velocidade.')