'''
Ex. 68.  Faça um programa que jogue par ou impa com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
v= 0

while True:
    jogador = int(input('Digite um Valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'IP':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v = v + 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v = v + 1
        else:
            print('Você PERDEU!')
            v = v + 1
            break
    print('Vamos jogar novamente...')
    print(f'GAME OVER! Você venceu {v} vezes.')

