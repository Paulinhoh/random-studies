"""
    Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando espaçoes.
    Ex.: apos a sopa, a torre da derrota.
"""

frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')

frase_invertida = ''
for caractere in frase:
    frase_invertida = caractere + frase_invertida

# frase_invertida = frase[::-1]  -> outra forma de inveter a frase

if frase == frase_invertida:
    print('É um PALINDROMO')
else:
    print('Não é um PALINDROMO')
