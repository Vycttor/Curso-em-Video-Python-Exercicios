'''
Ex 67. Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuário. O programa será interropido quando o número solicitado for negativo.
'''



while True:
    print('=='*25)
    t = int(input('Informe a tabuada que deseja: '))
    
    if t < 0:
        break
    for c in range(0,11):      
        #print(f'|{num} X {c}  = {resultato}|')
        print("{} X  {} = {} ".format(t,c, t*c))       
    print('=='*25)
    print('**Iforme um valor negativo para ENCERRAR')
    
print('Programa encerrado')