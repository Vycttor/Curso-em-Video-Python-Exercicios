'''
Ex 49. Refaça o desafio 009, mosntrando a tabuada que o usuário escolher, só que agora utilizando um laço for.
'''

#Código feito dia 11/11/2024
#Código feito meio certo, corrigido para versão do Prof. Guanabara, sitaxe melhor. 

#solicia para o usuario informar qual tubuada deseja calcular.
print('=='*20)
num = int(input('Informe a tabuada que deseja:Nº '))
print('=='*20)

#Condição realiza o calculo em loop até a posição solicitada.
for c in range(0,11):      
        #print(f'|{num} X {c}  = {resultato}|')
        print("{} X  {} = {} ".format(num,c, num*c))


  