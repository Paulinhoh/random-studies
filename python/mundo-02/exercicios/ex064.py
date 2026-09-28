"""
    Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar
    quando o usuario digitar o valor 999, que é a condição de parada. No final mostre quantos numeros
    foram digitados e qual foi a soma entre eles.
"""

resp = 0
soma = 0
qt_elementos = 0
while resp != 999:
    resp = int(input('Digite um valor: '))

    if resp != 999:
        soma += resp
        qt_elementos += 1


print(f'Quantidade de numeros digitados: {qt_elementos}')
print(f'Soma dos elementos: {soma}')
