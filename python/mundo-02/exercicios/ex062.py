"""
    Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns
    termos. O programa encerra quando ele disser que quer mostrar 0 termos
"""

termos = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 10
continuar = True
while continuar:
    print(termos, end=' ')
    termos += razao

    contador -= 1
    if contador < 1:
        resp = int(input('\nQuer ver mais quantos termos: '))

        if resp < 1:
            print('Saindo...')
            continuar = False
        else:
            contador = resp
