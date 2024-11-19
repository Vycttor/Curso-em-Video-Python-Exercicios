'''
Ex 057. Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,  peça a digitação novamente até ter um valor correto.
'''

sexo = ['m','f']


while True:
    n = str(input('Digite o sexo [M/F]: ')).strip().lower()