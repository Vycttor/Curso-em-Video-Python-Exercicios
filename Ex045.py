'''
Ex.45 Crie um programa que faça o computador jogar JOKENPÔ com você.

PEDRA, PAPEL e TESOURA.
'''

#Programa feito pelo Prof: Gustavo Guanabara.
#Programa feito dia: 04/11/2024.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2) # randint vair sortear aelatoriamente os itens, da posição 0 a 2.

print('''Sua opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA ''')

jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador == 2:
         print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')   
    else:
        print('JOGADA INVÁLIDA')