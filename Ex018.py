# Ex018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do Seno, cosesno e tangente desse ângulo.

# 15/10/2024, Não consegui resolver esse exercicio. A resposta abaixo é do video explicativo do professor Guanabara Curso em Video.

# Importa do modulo math, os seguintes metodos.
from math import radians, sin, cos, tan

#Solicita para o usuario informar o ângulo desejado.
angulo = float(input('Digite o ângulo que você deseja: '))

#Calculo do ângulo utilizando os metodos.

seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

cosseno = sin(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosseno))

tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))

