'''
Ex. 48 Faça um programa que calcule a soma entre os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

    
'''
L = list(range(1, 501, 2))
print(L)
soma = sum(L)
print(f'A soma dos valores da lista é = {soma}') 
print('\n')  
'''
#Código feito pelo Prof. Gustavo.
        
soma = 0  #Acumulador 
cont = 0 #Contador

for c in range(1,501,2):
    if c % 3 == 0:# Números divisiveis por 3.
        cont +=  1
        soma +=  c        
print(f'A soma de todos {cont}  os valores solicitados é {soma}')
        


    

  