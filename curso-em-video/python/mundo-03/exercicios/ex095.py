"""
    Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

jogadores = []
while True:
    jogador = {}
    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['partidas'] = int(
        input('Digite o número de partidas que o jogador jogou: '))

    for i in range(jogador['partidas']):
        jogador[f'partida_{i+1}'] = int(
            input(f'Digite a quantidade de gols na partida {i+1}: '))

    jogador['total_gols'] = sum(
        [jogador[f'partida_{i+1}'] for i in range(jogador['partidas'])])

    jogadores.append(jogador)

    continuar = input('Deseja cadastrar outro jogador? (s/n): ').lower()
    if continuar != 's':
        break

print(jogadores)
