'''
Ex. 59. Crie umprograma que leia dois valores e mostre um menu na tela:

[1] SOMA
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA

Seu programa deverá realizar a operação solicitada em cada caso.
'''

valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite o segundo valor: '))
menu = 0

#aprendendo laços
while menu != 5:
    print('''
    [1] SOMA
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRMA''')

    menu = int(input('Escolha uma opção do MENU: Nº'))
    if menu == 1:
        soma = valor_1 + valor_2
        print(f'A soma de {valor_1} + {valor_2} = {soma}') 
    elif menu == 2:
        mult = valor_1 * valor_2
        print(f'A multiplicação entre {valor_1} x {valor_2} = {mult}')
    elif menu == 3:
        if valor_1 < valor_2:
            print("O número {} é maior".format(valor_2))
            print('O segundo valor é maior')
        if valor_1 > valor_2:
            print("O número {} é maior".format(valor_1))
            print(f'O primerio valor é maior')
        if valor_1 == valor_2:
            print(f'O númeo {valor_1} e o número {valor_2} são iguais') 
    elif menu == 4:
        valor_1 = int(input('Digite um valor: '))
        valor_2 = int(input('Digite o segundo valor: '))
          
    elif menu ==5:
        print('Finalizando')

    else:
        print('Opção inválida. Tente novamente')
print('Fim do programa')        
        


