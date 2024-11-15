# Ex006 Crie um algoritimo que leia um número e mostre o seu dobro, triplo
# e raiz quadrada.



n1 = int(input("Digite um numero: "))
print("\n")

#Calculo dodro do valor.
dobro = n1*2
print("O dobro de {} é =: {} ".format(n1,dobro))

#Calculo triplo do valor.
triplo = n1*3
print("O triplo de {} é =: {}".format(n1,triplo))

#Calaculo raiz quadrada.
raiz = n1**(1/2)
print("A raiz quadrada de {} é =: {:.0f} ".format(n1,raiz))
