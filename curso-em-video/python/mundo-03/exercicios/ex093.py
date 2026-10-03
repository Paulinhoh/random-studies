"""
    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = {}
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['partidas'] = int(
    input('Digite o número de partidas que o jogador jogou: '))

for i in range(jogador['partidas']):
    jogador[f'partida_{i+1}'] = int(
        input(f'Digite a quantidade de gols na partida {i+1}: '))

jogador['total_gols'] = sum(
    [jogador[f'partida_{i+1}'] for i in range(jogador['partidas'])])

print(jogador)
