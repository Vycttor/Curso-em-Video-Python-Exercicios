#Ex023 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um do dígitos separados.

#Ex: Digite um número: 1834

#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
#Exercicio resolvido pelo professor Guanabara, infelizmente não consegui resolver esse com meus conhecimento atuais.
num = int(input("Digite um numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 100 % 10

print('Analisa o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Cententa: {}'.format(c))
print('Milhar: {}'.format(m))