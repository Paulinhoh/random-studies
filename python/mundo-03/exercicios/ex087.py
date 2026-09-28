"""
    Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados;
    B) A soma dos valores da terceira coluna;
    C) O maior valor da segunda linha.
"""

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para a posição [{i}, {j}]: '))
        linha.append(valor)
    matriz.append(linha)

# A) A soma de todos os valores pares digitados
soma_pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            soma_pares += valor

# B) A soma dos valores da terceira coluna
soma_terceira_coluna = 0
for i in range(3):
    soma_terceira_coluna += matriz[i][2]

# C) O maior valor da segunda linha
maior_segunda_linha = matriz[1][0]
for j in range(1, 3):
    if matriz[1][j] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][j]

print(f'A) A soma de todos os valores pares digitados: {soma_pares}')
print(f'B) A soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'C) O maior valor da segunda linha: {maior_segunda_linha}')
