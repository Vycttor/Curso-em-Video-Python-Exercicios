#Ex016 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex. Digite um número: 6.127 O número 6.127 tem a parte inteira 6.

#Foi importada a biblioteca math para uso dos recursos da biblioteca.
import math

#Solicita para o usúario digitar um numero real.
num = float(input('Digite um numero real: '))
# Printa na tela i número real de de forma inteira, utilizando math.floor da biblioteca math.
print('O numero real {}, >>> forma inteira {} '.format(num,math.floor(num)))
