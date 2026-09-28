"""
    Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo
    de 10 até 0, com uma pause de 1s entre eles.
"""

import time

print('Contagem regressiva para os Fogos:')
for i in range(10, -1, -1):
    time.sleep(1)
    print(i)
