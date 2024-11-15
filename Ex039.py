# Ex.039 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

#- Se ele ainda vai se alistar ao serviço militar.
#- Se é hora de se alistar.
#- Sé já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#Código feito dia 30/10/2024.
#Programa feito  abaixo, não está totalmente certo, devindo estar faltando informações adicionais.
#A partir da linha 34 segue programa corrigido pelo Prof. Gustavo Guanabara. 04/11/2024.

'''
print('=='*18)
nome = str(input('Digite seu nome: '))
idade = int(input('Informe sua idade: '))
print('=='*18)
print('\n')
print('=='*18)
if idade == 18:
    print(f'Olá {nome}, sua idade é obigatório o alistamento.')
    print(f'Acesse o site  alistamento.eb.mil.br, para mais informações.')
    print('=='*18)
elif idade < 18:
    print(f'Olá {nome}, você ainda não tem idade para se alistar.')
    print('Mas fique atento, pois com 18 anos é obrigatorio o alistamento.')
    print(f'O alistamento militar obrigatório deve ser feito no primeiro semestre\n do ano em que o jovem completa 18 anos de idade. O prazo para o alistamento é de janeiro a junho.')
    print('=='*18)
elif idade > 18:
    print(f'Olá {nome}, como você já tem mais de 18 anos, infelizmente já passou do prazo para se alistar.')
    print('A multa para quem não se alistar dentro do prazo é de R$ 5,91.')
    print('Acesse o site  alistamento.eb.mil.br, para mais informações.')    
    print('=='*18)
'''

from datetime import date

ano_de_nascimento = int(input('Informe seu ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento

print(f'Quem nasceu em {ano_de_nascimento} tem {idade} anos em {ano_atual}')

if idade == 18:
    print('você tem que alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = ano_atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos')
    ano_de_alisatamento = ano_atual - saldo
    print(f'Seu alistamento foi em {ano_de_alisatamento}')

 

