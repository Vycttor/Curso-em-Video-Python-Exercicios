'''
Ex. 55. Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

#Código feito pelo professor Guanabara.
#Minha parte ficou 30% certo.
maior = 0
menor = 0

for c in range(1, 6 ):
    peso  = float(input('Informe o peso Kg da {}ª  pessoa: '.format(c)))
    
    if c == 1:
        maior = peso 
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso    
      
print(f'O maior peso lido foi de {maior} Kg')
print(f'O menot peso lido foi de {menor} Kg') 