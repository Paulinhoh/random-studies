"""
    Faça um programa que tenha uma função chamada escreva(), que receba um texto como parâmetro e mostre uma mensagem com tamanho adaptável.
"""


def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)


escreva('Olá, Mundo!')
