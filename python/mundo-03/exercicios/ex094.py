"""
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas;
    B) A média de idade do grupo;
    C) Uma lista com todas as mulheres;
    D) Uma lista com todas as pessoas com idade acima da média.
"""

pessoas = []
while True:
    pessoa = {}
    pessoa['nome'] = input('Digite o nome da pessoa: ')
    pessoa['sexo'] = input('Digite o sexo da pessoa (M/F): ').upper()
    while pessoa['sexo'] not in ['M', 'F']:
        print('Sexo inválido! Digite M ou F.')
        pessoa['sexo'] = input('Digite o sexo da pessoa (M/F): ').upper()
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    pessoas.append(pessoa)

    continuar = input('Deseja continuar? (S/N): ').upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida! Digite S ou N.')
        continuar = input('Deseja continuar? (S/N): ').upper()
    if continuar == 'N':
        break

print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')

# Calcular a média de idade
soma_idades = sum([p['idade'] for p in pessoas])
media_idade = soma_idades / len(pessoas) if len(pessoas) > 0 else 0
print(f'Média de idade do grupo: {media_idade:.2f}')

# Listar todas as mulheres
mulheres = [p for p in pessoas if p['sexo'] == 'F']
print(f'Lista de mulheres: {[m["nome"] for m in mulheres]}')

# Listar todas as pessoas com idade acima da média
acima_media = [p for p in pessoas if p['idade'] > media_idade]
print(
    f'Lista de pessoas com idade acima da média: {[a["nome"] for a in acima_media]}')
