"""
    Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.

    :param n: Número a calcular o fatorial.
    :param show: Valor lógico indicando se será mostrado o processo de cálculo.
    :return: Fatorial do número n.
    """
    if n < 0:
        return None  # Fatorial não definido para números negativos
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(n, 0, -1):
            resultado *= i
            if show:
                print(i, end=' ')
                if i > 1:
                    print('x', end=' ')
        if show:
            print('= ', end='')
        return resultado


# Testando a função
numero = int(input('Digite um número para calcular o fatorial: '))
mostrar = input('Deseja mostrar o processo de cálculo? (s/n): ').lower() == 's'
resultado = fatorial(numero, mostrar)
if resultado is not None:
    print(resultado)
