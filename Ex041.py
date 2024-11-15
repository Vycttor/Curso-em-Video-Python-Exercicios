#Ex.41 A Confederação nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

#Código feito dia 31/10/2024
#Feito update no código, foi implementado o módulo datetime para pegar o ano atual.


from datetime import date
#Variaveis globais.


print('=='*20)
ano_informado = int(input('Informe o ano de nascimento do atleta: '))

ano_atual = date.today().year
idade_atleta = ano_atual - ano_informado
print('=='*20)
print(f'Idade atleta: {idade_atleta} anos.')

if idade_atleta <= 9.00:
    print('Categoria MIRIM')
    print('=='*20)
elif idade_atleta > 20.10:
    print(f'Categoria MASTER')
elif idade_atleta >= 19.10 and 20.00:
    print(f'Categoria SENIOR')
    print('=='*20)
elif idade_atleta >= 14.10 and 19.00:
    print(f'Categoria JUNIOR')
elif idade_atleta >= 9.10 and  14.00:
    print('Categoria INFANTIL')
    print('=='*20)



