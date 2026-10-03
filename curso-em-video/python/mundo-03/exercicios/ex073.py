"""
    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    A) Apenas os 5 primeiros colocados.
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética.
    D) Em que posição na tabela está o time da Chapecoense.
"""

tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
          'América-MG', 'Botafogo', 'Santos', 'São Paulo', 'Bragantino', 'Ceará', 'Atlético-GO', 'Coritiba', 'Fortaleza', 'Goiás', 'Avaí', 'Juventude', 'Cuiabá')

print('=-' * 20)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('=-' * 20)

print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print('=-' * 20)

print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print('=-' * 20)

print(f'O time da Chapecoense está na posição: {tabela.index("Chapecoense") + 1}')
