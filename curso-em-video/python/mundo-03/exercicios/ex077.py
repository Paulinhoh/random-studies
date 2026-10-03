"""
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('python', 'programacao', 'desenvolvimento', 'tupla', 'exercicio')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
    print()
