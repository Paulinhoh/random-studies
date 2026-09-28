"""
    Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista, ja na posicao correta de insercao (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = []
for i in range(5):
    n = int(input('Digite um valor: '))
    if not lista:
        lista.append(n)
    else:
        for j in range(len(lista)):
            if n < lista[j]:
                lista.insert(j, n)
                break
        else:
            lista.append(n)

print(f'Valores digitados em ordem crescente: {lista}')
