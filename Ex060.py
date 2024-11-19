'''
Ex. 60. Faça um programa que leia um número qualquer e mostre o seu fatorial

Fatorial de 5.
Ex: 5! = 5x4x3x2x1 = 120
'''


fat = 1
cont =1

numero = int(input('Informe o numero: '))

while cont <= numero:

    fat *= cont
    #print(fat)
    cont += 1
    
print(f'{numero}! = {fat}')    
print('fim')
  
