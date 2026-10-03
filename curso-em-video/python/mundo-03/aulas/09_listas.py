# =--=-=--=-=-=-=-=-=-=-=-= Listas I =--=-=--=-=-=-=-=-=-=-=-=

num = [1, 2, 3, 4, 5]
print(num)

num[0] = 10
num.append(6)
num.sort(reverse=True)
num.insert(2, 15)

print(num)
print(f'Essa lista tem {len(num)} elementos.')

num.remove(15)
if 4 in num:
    num.remove(4)
print(num)

num.pop()
print(num)

for n in num:
    print(n, end=' ')

print()

a = [2, 3, 4, 7]
b = a[:]  # Copiando a lista a para b
b[2] = 8
print(f'\nLista A: {a}')
print(f'Lista B: {b}')
print('=-='*20)


# =--=-=--=-=-=-=-=-=-=-=-= Listas II =--=-=--=-=-=-=-=-=-=-=-=

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])

pessoas = list()
pessoas.append(dados[:])
pessoas.append(['Maria', 19])
pessoas.append(['João', 32])
print(pessoas)

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
