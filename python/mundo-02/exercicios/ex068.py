"""
    Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

escolhas = ['par', 'impar']
vitorias_consecutivas = 0

while True:
    numero_jogador = int(input("Digite um número: "))
    jogador = input("Escolha par ou impar: ").lower()
    if jogador not in escolhas:
        print("Escolha inválida. Tente novamente.")
        continue

    computador = randint(1, 10)
    print(f"Computador jogou: {computador}")

    if (numero_jogador + computador) % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'

    print(f"Resultado: {numero_jogador + computador} é {resultado}")

    if jogador == resultado:
        print("Você venceu!")
        vitorias_consecutivas += 1
    else:
        print("Você perdeu!")
        break

print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")
