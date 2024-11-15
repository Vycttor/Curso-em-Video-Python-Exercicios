'''
Ex. 54. Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores. OBS: Considerar a maioridade com 21 anos.
'''
#Código feito pelo Prof. Gustavo.
from datetime import date
#variavel global
atual = date. today().year

#Variaveis contadoras.
totmaior = 0
totmenor = 0

for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))