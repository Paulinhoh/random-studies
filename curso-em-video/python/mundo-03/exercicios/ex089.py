"""
    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

alunos = []
while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    if continuar != 'S':
        print('Opção inválida. Encerrando o programa.')
        break
    if continuar == 'S':
        continue
    break

print('\nBoletim:')
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

print('\nPara ver as notas de um aluno específico, digite o número do aluno.')
while True:
    try:
        num_aluno = int(input('Número do aluno (ou 999 para sair): '))
        if num_aluno == 999:
            break
        if 0 <= num_aluno < len(alunos):
            print(f'Notas de {alunos[num_aluno][0]}: {alunos[num_aluno][1]}')
        else:
            print('Aluno não encontrado.')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número.')
