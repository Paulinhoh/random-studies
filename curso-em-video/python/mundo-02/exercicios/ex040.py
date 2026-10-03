"""
    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
    uma mensagem no final, de acordo com a media atingida.
    - media abaixo de 5: REPROVADO
    - media entre 5 e 6.9: RECUPERAÇÃO
    - media 7 ou superior: APROVADO
"""

nota01 = float(input('Digite a 1° nota do aluno: '))
nota02 = float(input('Digite a 2° nota do aluno: '))
media = (nota01 + nota02) / 2

if media < 5:
    print(f'Media: {media}')
    print('REPROVADO')
elif media >= 5 and media < 7:
    print(f'Media: {media}')
    print('RECUPERAÇÃO')
else:
    print(f'Media: {media}')
    print('APROVADO')
