#Ex.35 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Exercicio resolvido pelo Prf. Gustavo dia 25/10/2024.

print("-="*20)
print('Analisador de Triângulo')
print("-="*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

