# =--=-=--=-=-=-=-=-=-=-=-= Dicionarios =--=-=--=-=-=-=-=-=-=-=-=

dados = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
dados['peso'] = 75.5  # Adicionando um novo par chave-valor
dados['idade'] = 26  # Atualizando o valor associado à chave 'idade'
print(dados['nome'])  # Acessando o valor associado à chave 'nome'
print(dados['idade'])  # Acessando o valor associado à chave 'idade'
print(dados['sexo'])  # Acessando o valor associado à chave 'sexo'
print(dados['peso'])  # Acessando o valor associado à chave 'peso'
print(dados)
del dados['idade']  # Removendo o par chave-valor com a chave 'idade'
print(dados)  # Exibindo o dicionário atualizado

print('=-=' * 20)
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme.values())  # Exibindo os valores do dicionário
print(filme.keys())  # Exibindo as chaves do dicionário
print(filme.items())  # Exibindo os pares chave-valor do dicionário

for key, value in filme.items():  # Iterando sobre os pares chave-valor do dicionário
    # Exibindo cada chave e seu valor correspondente
    print(f'O {key} é {value}')

print('=-=' * 20)

locadora = []
# Adicionando o dicionário 'filme' à lista 'locadora'
locadora.append(filme.copy())
# Adicionando outro dicionário à lista
locadora.append({'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'})
# Adicionando mais um dicionário à lista
locadora.append({'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Lana Wachowski'})
print(locadora)  # Exibindo a lista 'locadora' atualizada

# Acessando o título do primeiro filme na lista 'locadora'
print(locadora[0]['titulo'])
