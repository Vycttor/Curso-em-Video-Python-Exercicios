'''
Ex 69. Crei um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

a) Quanta pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
'''

cont_h = cont_m = cont_idade = 0

while True: 
    idade = int(input('Informe a idade: '))
    sexo = ' ' 
    while sexo not in 'mf': # laço não permite avaçar enquanto não for digitado o valor correto do tipo.
        sexo = str(input('Informde o sexo:[M/F]')).strip().lower()

    if idade >= 18:
        cont_idade = cont_idade + 1

    if sexo  == 'm':
        cont_h = cont_h + 1

    if idade < 20 and sexo == 'f':
        cont_m = cont_m + 1

    continuar = ' '
    while continuar not in 'sn': #Condição de parada usando o tipo. 
        continuar = str(input('Continuar:[S/N] '))
    if continuar == 'n': # Casso for digitado n, se torna verdadeiro e sai do laço.
        break

print(f'Total de pessas com mais de 18 anos: {cont_idade}')
print(f'Ao todo temos {cont_h} homens cadastrados')
print(f'E temos {cont_m} mulheres com menos de 20 anos')


    