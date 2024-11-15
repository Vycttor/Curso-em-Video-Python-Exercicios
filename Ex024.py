#Ex024 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

#Exercicio resolvido pelo professor Gustavo Guanabara.
cid = str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
