"""
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


# Testando a função
ano = int(input('Digite o ano de nascimento: '))
resultado = voto(ano)
print(f'Com {date.today().year - ano} anos: Voto {resultado}.')
