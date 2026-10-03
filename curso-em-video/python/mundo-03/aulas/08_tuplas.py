# =--=-=--=-=-=-=-=-=-=-=-= Tuplas =--=-=--=-=-=-=-=-=-=-=-=

# tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas.

lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
print(lanche[1])  # suco
print(lanche[-2])  # pizza
print(lanche[1:3])  # ('suco', 'pizza')

print(lanche.index('pizza'))  # 2

print(len(lanche))  # 4
print(sorted(lanche))  # ['hambúrguer', 'pizza', 'pudim', 'suco']

print('=-' * 20)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('=-' * 20)
for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}')

print('=-' * 20)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

del (lanche)  # deleta a tupla lanche
