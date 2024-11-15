#Ex.38 Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:

#- O primeiro valor é maior
#- O Segundo valor é maior
#- Não existe valor maior, os dois são iguais.

#Data: Programa feito dia 30/10/2024.
#Atualizção upgrade feito dia 04/11/2024, foi acrescentado prints informativos.

#Solicita para o usuario informar os números para ser feito a comparação.
numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo número: '))

#Condição If, reaaliza a comparação dos numeros conforme a regra.
if numero_1 < numero_2:
    print("O número {} é maior".format(numero_2))
    print('O segundo valor é maior')
elif numero_1 > numero_2:
     print("O número {} é maior".format(numero_1))
     print(f'O primerio valor é maior')
elif numero_1 == numero_2:
    print(f'O númeo {numero_1} e o número {numero_2} são iguais')