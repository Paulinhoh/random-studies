"""
    Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)
"""


def notas(*notas, situacao=False):
    """
    Função que recebe várias notas de alunos e retorna um dicionário com informações sobre as notas.

    :param notas: Notas dos alunos (quantidade variável).
    :param situacao: Indica se a situação da turma deve ser incluída no dicionário (opcional).
    :return: Dicionário com informações sobre as notas.
    """
    resultado = {}
    resultado['quantidade'] = len(notas)
    resultado['maior'] = max(notas) if notas else None
    resultado['menor'] = min(notas) if notas else None
    resultado['media'] = sum(notas) / len(notas) if notas else None

    if situacao:
        if resultado['media'] is not None:
            if resultado['media'] >= 7:
                resultado['situacao'] = 'Aprovado'
            elif resultado['media'] >= 5:
                resultado['situacao'] = 'Recuperação'
            else:
                resultado['situacao'] = 'Reprovado'
        else:
            resultado['situacao'] = 'Sem notas para avaliar'

    return resultado


# Testando a função
notas_alunos = notas(8.5, 7.0, 9.0, 6.5, situacao=True)
print(notas_alunos)
