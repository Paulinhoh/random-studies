"""
    Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

termos = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 10
while contador > 0:
    print(termos, end=' ')
    termos += razao
    contador -= 1
