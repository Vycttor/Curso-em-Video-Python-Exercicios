'''
Ex 066. Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

cont = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    cont = cont + 1
    soma = soma + numero

print(f'Foram digitados {cont} números')
print(f'A soma dos números é: {soma}') 