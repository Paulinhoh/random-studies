"""
    Refaça o exercicio 035 dos triangulos, acecentando o recurso de mostrar que tipo de triangulo sera formado:
    - Equilatero: todos os lados iguais
    - Isosceles: dois lados iguais
    - Escaleno: todos os lados diferentes
"""

a = int(input('digite a 1° reta: '))
b = int(input('digite a 2° reta: '))
c = int(input('digite a 3° reta: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('Podem formar um triangulo', end=' ')
    if a == b and a == c:
        print('Equilatero')
    elif a == b or a == c or b == c:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Não podem formar um triangulo!')
