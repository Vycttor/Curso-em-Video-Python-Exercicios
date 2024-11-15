# Ex005 Faça um programa que leia um número inteiro e mostre na tela
# o seu sucessor e seu antecessor.


print("PROGRAMA MOSTRA O NUMERO SUCESSOR E ANTECESSOR\n")
n1 = int(input("Digite um numero: "))

ant = n1-1
suc = n1+1

print(" O valor antecessor é {} e o sucessor é {}".format(ant,suc))