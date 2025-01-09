'''
Ex. 73 Crie uma tupla preenchida com os 20 primerios colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados na tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
'''

times_brasileirao_2019 = (
    'Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Athletico-PR',
    'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
    'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo',
    'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'
)
#método sorted permite ordenar a tupla em ordem alfaética.

ordem_alfabetica = sorted(times_brasileirao_2019)

print('\n')
print('===='*15)
print(f'Os 5 primeiros colocados são: {times_brasileirao_2019[0:5]}')
print('===='*15)
print(f'Os 4 ultimos colocados são: {times_brasileirao_2019[16:20]}')
print('===='*15)
print(f'Times em ordem alfabética: {ordem_alfabetica}')
print('===='*15)
print(f'A {times_brasileirao_2019[18]} encontra-se na 19º posição')
print('===='*15)