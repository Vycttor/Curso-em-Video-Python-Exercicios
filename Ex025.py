#Ex025 Crie um pograma que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#Exercicio resolvido pelo Prof. Gustavo Guanabara.

nome = str(input('Qual é seu nome completo? ')).strip()

print('Seu nome tem Silva {}'.format('silva' in nome.lower()))