'''
Ex 56. Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 quatro pessoas. No final do programa, mostre:

> A média de idade do grupo.
> Qual é o nome do homem mais velho.
> Quantas mulheres têm menos de 20 anos.
'''

#Exercicio resolvido com auxilio Prof: Guanabara.

somaidade = 0
mediaidade = 0
maioridadedehome = 0
nomevelho = ''
totmulher = 0

for p in range(1,5):
    print(f'----- {p}ª-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadedehome = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehome:
        maioridadedehome = idade
        nomevelho = nome
    if sexo in 'Fn' and idade < 20:
        totmulher += 1
     
mediaidade = somaidade / 4
print(f'A media idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadedehome} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos')


