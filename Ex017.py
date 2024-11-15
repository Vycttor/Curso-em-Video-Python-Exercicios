# Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.


# (H²) = (ct²)+(ct²) / Fómula calculo para acha o comprimento da hipotenuza.
#Função calcula os catetos, para obeter o comprimento da hipotenusa.
def comprimento(cat_1,cat_2):
    import math
    cateto1 = pow(cat_1,2)
    #print(cateto1) 
    cateto2 = pow(cat_2,2)
    #print(cateto2) 
    somacatetos = cateto1+cateto2
    print('O compremento da Hipotenusa é {:.2f} cm'.format(math.sqrt(somacatetos)))
    #Outro metodo é o uso do método hypot, que já calcula diretamento a hipotenusa, sem conceito da lógica// Essa linha de código foi implementada dia 14/10/2024.
    somacatetos = math.hypot(cat_1,cat_2)
    print('A hipotenusa mede {:.2f} cm'.format(somacatetos))

# Solicita para o usúario fornecer os catetos, para realização do calculo.
cat_1 = float(input('Digite o cateto oposto: '))
cat_2 = float(input('Digite o cateto adjacente: '))

#Chama a função que calcula o compremente da hipotenusa
comprimento(cat_1,cat_2)
