"""
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    A) Quantas pessoas tem mais de 18 anos.
    B) Quantos homens foram cadastrados.
    C) Quantas mulheres tem menos de 20 anos.
"""
qtd_maiores = 0
qtd_homens = 0
qtd_mulheres_menores = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()

    if idade > 18:
        qtd_maiores += 1

    if sexo == "M":
        qtd_homens += 1

    if sexo == "F" and idade < 20:
        qtd_mulheres_menores += 1

    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar == "N":
        break

print(f"Quantidade de pessoas com mais de 18 anos: {qtd_maiores}")
print(f"Quantidade de homens cadastrados: {qtd_homens}")
print(f"Quantidade de mulheres com menos de 20 anos: {qtd_mulheres_menores}")
