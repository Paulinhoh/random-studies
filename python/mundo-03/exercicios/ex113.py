"""
    Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
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


def leiaFloat(msg):
    """
    Função que solicita ao usuário um número real, validando a entrada.

    :param msg: Mensagem a ser exibida para o usuário.
    :return: Número real digitado pelo usuário.
    """
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('ERRO! Digite um número real válido.')


# Testando a função
numero = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número: {numero}')

numero_real = leiaFloat('Digite um número real: ')
print(f'Você digitou o número: {numero_real}')
