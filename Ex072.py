'''
Ex 72 Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (etre 0 e 20) e mostrá-lo por extenso.

'''

cont = ('zero', 'Um', 'Dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catoze', 'quinze', 
         'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')

while True:
    numero = int(input('Digite um numero Nº: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[numero]}')