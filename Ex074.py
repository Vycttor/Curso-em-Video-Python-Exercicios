'''
Ex. 74 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: ', end=' ') 

for c in numeros:
    print(f'{c}', end=' ')

print(f'\n O maior valor sorteado foi: {max(numeros)}')
print(f'Omenor valor sorteado foi: {min(numeros)}')