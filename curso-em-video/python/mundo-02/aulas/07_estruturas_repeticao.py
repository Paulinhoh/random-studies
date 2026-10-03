# =--=-=--=-=-=-=-=-=-=-=-= Estrutura de repetição for =--=-=--=-=-=-=-=-=-=-=-=

for i in range(1, 11):
    print(i)
print()

for i in range(0, 11, 2):
    print(i)
print()

for i in range(10, 0, -1):
    print(i)


# =--=-=--=-=-=-=-=-=-=-=-= Estrutura de repetição while =--=-=--=-=-=-=-=-=-=-=-=

count = 1
while count < 10:
    print(count)
    count += 1


# =--=-=--=-=-=-=-=-=-=-=-= Interrompendo repetições while =--=-=--=-=-=-=-=-=-=-=-=

# loop infinito
while (True):
    break  # interrompe o loop

while (True):
    number = 1
    if number == 1:
        print('entrou no continue')
        continue  # continue ele pula o resto da execução e volta ao inicio do loop

    print('resto da execuçã')

    if number == 3:
        print('entrou no break')
        break

    number += 1
