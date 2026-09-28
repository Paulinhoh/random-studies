"""
    Desenvolva um programa que leia nome, idade e sexo de 4 pessoa. No final do programa mostre:
    - A media de idade do grupo
    - qual o nome do homem mais velho
    - quantas mulheres tem menos de 20 ano
"""

mulheres_menores_de_20 = 0
homem_mais_velho = ''
maior_idade = 0
soma_idades = 0

for i in range(1, 5):
    nome = str(input(f'Digite o nome da {i}° pessoa: '))
    idade = int(input(f'Digite o idade da {i}° pessoa: '))
    sexo = str(input(f'Digite o sexo da {i}° pessoa: [M/F]')).upper()[0]

    if sexo == 'F' and idade < 20:
        mulheres_menores_de_20 += 1
    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            homem_mais_velho = nome

    soma_idades += idade

media_idade = soma_idades / 4

print(f' media de idade do grupo é: {media_idade}')
print(f' o homem mais velho é: {homem_mais_velho}')
print(
    f' quantidade de mulheres com menos de 20 anos: {mulheres_menores_de_20}')
