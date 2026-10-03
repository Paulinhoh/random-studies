"""
    Crie um programa que leia dois valores e mostre um menu na tela:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa
    Seu programa devera realizar a operação solicitada em cada caso.
"""

from time import sleep

num1 = int(input('Digite um valor inteiro: '))
num2 = int(input('Digite outro valor inteiro: '))

continuar = True
while continuar:
    sleep(1)

    print("""[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa""")
    opcao = int(input('-> '))

    if opcao == 1:
        print(f'Soma dos valores: {num1+num2}')
    elif opcao == 2:
        print(f'Multiplicação dos valores: {num1*num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior valor é: {num1}')
        elif num2 > num1:
            print(f'O maior valor é: {num2}')
        else:
            print('Os valores são iguais')
    elif opcao == 4:
        print('Novos valores.')
        num1 = int(input('Digite o novo valor inteiro: '))
        num2 = int(input('Digite outro valor inteiro: '))
    elif opcao == 5:
        print('Saindo...')
        continuar = False
    else:
        print('Opção invalida! Tente novamente.')
