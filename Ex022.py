#Ex 22 Crie um programa que leia o nome completo de uma pessoa e mostre.

#O nome com todas as letras maiúscula.
#O nome com todos as letras minúsculas.
#Quantas letras ao todo(sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

#O nome com todas as letras maiúscula.
print('O seu nome em letras maiusculas é: {} '.format(nome.upper()))
#O nome com todos as letras minúsculas.
print('O seu nome em letras minusculas é: {}'.format(nome.lower()))
#Quantas letras ao todo(sem considerar espaços).
print('O seu nome tem ao todo {} letras '.format(len(nome) - nome.count(' ')))    
#Quantas letras tem o primeiro nome.
nome1 = nome.split() #Aqui trabalha o conceito de lista, atenção.
# nome1[] virou lista, onde cada paravra dentro da lista tem uma posição.
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome1[0], len(nome1[0])))