# Ex.37 Escreva um programa que leia um númeo inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

#-1 para binário
#-2 para octal
#-3 para hexadecimal


# Programa resolvido pelo Prof. Gustavo.


#Solicita para o usuario, informar o número desejado para conversão.
num = int(input('Digite um número interiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é ugual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é ugual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é ugual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')