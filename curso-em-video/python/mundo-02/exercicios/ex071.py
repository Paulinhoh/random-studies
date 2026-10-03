"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
valor = int(input("Qual o valor a ser sacado? R$"))

cedulas = [50, 20, 10, 1]
quantidades = []

for cedula in cedulas:
    quantidade = valor // cedula
    quantidades.append(quantidade)
    valor %= cedula

print("Cédulas entregues:")
for i in range(len(cedulas)):
    if quantidades[i] > 0:
        print(f"{quantidades[i]} cédula(s) de R${cedulas[i]}")
