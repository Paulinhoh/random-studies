frase = 'Curso em Video Python'

# =-=-=-=-=-=-=-=-==-=-=-=-= Fatiamento =-=-=-=-=-=-=-=-==-=-=-=-=
print(frase[9])
print(frase[15:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# =-=-=-=-=-=-=-=-==-=-=-=-= Analize =-=-=-=-=-=-=-=-==-=-=-=-=
print(len(frase)) # tamanho

print(frase.count('o')) # conta quantos vezes aparece o elemento
print(frase.count('o', 0, 13)) # conta quantos vezes aparece o elemento no fatiamento

print(frase.find('deo')) # mostra a posição onde esta o elemento
print(frase.find('Android')) # como não existe na frase retorna -1

print('curso' in frase) # retorna True or False, de acordo se existe o elemento na frase

# =-=-=-=-=-=-=-=-==-=-=-=-= Transformação =-=-=-=-=-=-=-=-==-=-=-=-=
frase.replace('Python', 'Android') # troca a plavra por outra
frase.upper() # maiusculas
frase.lower() # minusculas
frase.capitalize() # maiuscula só a primeira letra da frase
frase.title() # maiuscula as primeiras letras de cada palavra da frase
frase.strip() # remove os espaços da inicio e do final da frase
frase.rstrip() # remove os espaços da direita da frase
frase.lstrip() # remove os espaços da esquerda da frase

# =-=-=-=-=-=-=-=-==-=-=-=-= Divisão =-=-=-=-=-=-=-=-==-=-=-=-=
frase.split() # divide a frase pelos espaços
frase.split(',') # divide a frase pelos elementos escolhidos

# =-=-=-=-=-=-=-=-==-=-=-=-= Junção =-=-=-=-=-=-=-=-==-=-=-=-=
' '.join(frase) # junta colocando espaços entre as frases
