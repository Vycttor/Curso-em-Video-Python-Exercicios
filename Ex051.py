'''
Ex 51. Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

#Código feito pelo Prof. Gustavo 

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
# Fórmula 
decimo = primeiro +(10-1) * razao

for c in range(primeiro, decimo+razao, razao):
    print('{}'.format(c), end = '-> ')
print('ACABOU')    