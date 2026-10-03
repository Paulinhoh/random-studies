"""
    Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a
    base de coversao:
    - 1 para binario
    - 2 para octal
    - 3 para hexadecimal
"""

num = int(input('Digite um numero inteiro: '))
print("""Escolha a opcao de conversão:
1 -> Binario
2 -> Octal
3 -> Hexadecimal""")
opcao = int(input('-> '))

if opcao == 1:
    print(f'{num} convertido para Binario -> {bin(num)}')
elif opcao == 2:
    print(f'{num} convertido para Octal -> {oct(num)}')
elif opcao == 3:
    print(f'{num} convertido para Hexadecimal -> {hex(num)}')
else:
    print('Opção Invalida! Tente novamente.')
