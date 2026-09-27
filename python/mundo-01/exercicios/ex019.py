"""
    Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um
    programa que ajude ele, lendo o nome deles e escrevendo o nome do aluno escolhido.
"""
from random import choice

alunos = ['Maria', 'Ana', 'Gabriel', 'Jose']
aluno_escolhido = choice(alunos)

print(f'Aluno escolhido: {aluno_escolhido}')
