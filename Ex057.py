'''
Ex 057. Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,  peça a digitação novamente até ter um valor correto.
'''
#validador feito com auxilio do Prof. Guanabara.

sexo = str(input('Informe seu sexo: [M/F] ')).strip().lower()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F]')).strip().lower()[0]
print(f'Sexo {sexo} registrado com sucesso')