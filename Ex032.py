# Ex.32 Faça um programa que leia um ano qualquer e mostre, se ele é BISSEXTO.

#Exercicio feito pelo professor, Gustavo dia 25/10/2024.

#Importa o módulo data.
from datetime import date

#Solicita para o usuário informar o o ano desejado ou digitar 0, para veriicar o ano atual.
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))

#Primeiro IF executa a condição 0, para verificar o ano atual.
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

