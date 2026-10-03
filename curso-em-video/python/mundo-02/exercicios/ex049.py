"""
    Refaça o desafio 009, mostrando a tabuada de un numero que o usuario escolher, só que agora utilizando
    um laço for.
"""

num = int(input('Digite o numero: '))
for i in range(1, 11):
    print(f'{num} x {i} == {num*i}')
