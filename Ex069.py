'''
Ex 69. Crei um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

a) Quanta pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
'''

cont_h = cont_m = cont_idade = 0

while True:
    sexo = str(input('Informe o sexo: ')).strip().lower()
    idade = int(input('Informe a idade: '))
    if sexo == 999 and idade ==999:
        break
    if idade >= 18:
        cont_idade = cont_idade + 1
    if sexo  == 'm':
        cont_h = cont_h + 1
    if idade <= 20 and sexo == 'f':
        cont_idade = cont_idade +1
        cont_m = cont_h + 1


print(f'A {cont_idade} maior de 18 anos')


    