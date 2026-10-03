"""
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico inteiro.
"""


def leiaInt(msg):
    """
    Função que solicita ao usuário um número inteiro, validando a entrada.

    :param msg: Mensagem a ser exibida para o usuário.
    :return: Número inteiro digitado pelo usuário.
    """
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')


# Testando a função
numero = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número: {numero}')
