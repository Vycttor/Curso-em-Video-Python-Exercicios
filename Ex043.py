#Ex.43 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

'''
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
Acima de 40: Obesidade mórbida
'''

'''
Pesquisa para desenvolvemeto do exercicio.

IMC= peso(kg)/altura(m)² 

(Tabela 2024) info acquired on 03/11/2024.
A tabela do Índice de Massa Corporal (IMC) de acordo com a OMS é a seguinte:
IMC inferior a 18,5 kg/m2: baixo peso
IMC entre 18,5 e 24,9 kg/m2: eutrofia (peso adequado)
IMC entre 25 e 29,9 kg/m2: sobrepeso
IMC entre 30 e 34,9 kg/m2: obesidade grau 1
IMC entre 35 e 39,9 kg/m2: obesidade grau 2
IMC superior a 40 kg/m2: obesidade extrema 

'''
#Código feito dia 03/11/2024.
import math

print('=='*15)
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
print('=='*15)

#Linha de teste, para validar as condições.
#imc = float(input('Infome os imc para teste: '))

#Bloco de codigo, realiza calculo do IMC.
print('=='*15)
altura_2 = math.pow(altura,2)
imc = peso / altura_2  
#print(f'{altura_2:.2f}')
print(f'Seu IMC é: {imc:.2f}')
print('=='*15)


if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, você está abaixo do Peso.')
    print('=='*15)
elif imc >= 40:
    print(f'Seu IMC é {imc:.2f}, obesidade extrema.')   
    print('=='*15) 
elif imc >= 35 and 39.9:
    print(f'Seu IMC é {imc:.2f}, obesidade grau 2.')
    print('=='*15)
elif imc >= 30 and 34.9:
    print(f'Seu IMC é {imc:.2f}, obesidade grau 1.') 
    print('=='*15)
elif imc >= 25 and 29.9:
    print(f'Seu IMC é {imc:.2f}, sobrepeso.')
    print('=='*15)
elif imc >= 18.5 and 24.9:
    print(f'Seu IMC é {imc:.2f}, eutrofia (peso adequado).')
    print('=='*15)
      
