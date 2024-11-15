# Ex.30 Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
#Código feito dia 23/10/24
#Código corrigido dia 25/10/2024

#Programa verifica se um o a 10 é IMPAR ou PAR.

numero = int(input('Digite um numero: '))

#Foi usado modulo pois ele pega o resto da divisão, para resultado 0 é par, para resultado 1 é impar. //OBS o Numero sempre tem que ser dividido por 2.
resultado = numero % 2

if resultado == 0:
    print('par')
else:
    print('impar')

    #Resolução abaixo não serve já que, só é possível verificar os numeros que estão dentro da lista.
    
'''''
Criado uma array lista, com numeros pares e impares.
impar = [1,3,5,7,9]
par = [0,2,4,6,8]
#Condição compara com a lista e verificar se o numero escolhido entre 0 e 10 é IMPAR  OU PAR.
if numero in impar:
    print("impar")
else:
  
    print('par')    
'''    