# =--=-=--=-=-=-=-=-=-=-=-= Funções I =--=-=--=-=-=-=-=-=-=-=-=

def mostrar_linha():
    print('-' * 40)


def mensagem(msg):
    mostrar_linha()
    print(f'{msg:^40}')
    mostrar_linha()


def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} é {s}')


def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


mensagem('Funções em Python')
soma(4, 5)
soma(8, 9)
contador(1, 2, 3, 4, 5)
contador(10, 20, 30)

mensagem('Valores dobrados')
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
mostrar_linha()


# =--=-=--=-=-=-=-=-=-=-=-= Funções II =--=-=--=-=-=-=-=-=-=-=-=
def contador2(*num):
    """
    -> Função que recebe uma quantidade indefinida de números e mostra na tela.
    :param num: Números a serem mostrados.
    """
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


def soma2(a=0, b=0, c=0):
    """
    -> Função que recebe três números e mostra a soma deles.
    :param a: Primeiro número.
    :param b: Segundo número.
    :param c: Terceiro número.
    """
    s = a + b + c
    print(f'A soma de {a} + {b} + {c} é {s}')


def soma3(*valores):
    """
    -> Função que recebe uma quantidade indefinida de números e mostra a soma deles.
    :param valores: Números a serem somados.
    """
    s = sum(valores)
    return s


help(contador2)
help(soma2)

soma2(3, 2, 5)
soma2(8, 4)
s = soma3(5, 2, 1, 7)
print(f'A soma dos valores é {s}')
