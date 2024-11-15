# Ex.28 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

#O Programa deverá escrever na tela se o usuário venceu ou perdeu.

#Importado o método random, para gerar números.
import random


#Criado uma função, contendo a condição If para gerar os numeros solicitados
def sorteio(numero):
    s = random.randint(0,5)
    if numero == s:
        print('O número sorteado é {}, igual ao número informado {} PARABÉNS'.format(s,numero))
    else:
        print('O número sorteado é {}, infelizmente você errou.'.format(s))    

numero = int(input('Informe um número de 0 a 5: nº '))
print("\n")

sorteio(numero)