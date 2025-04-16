# Ex008 Escreva um programa que leia um valor em metros e o exiba convertido 
# em centimetros e milímetros.

print("PROGRAMA CONVERTE UM VALOR EM CENTIMETROS E MILIMETROS\n")
print("\n")
n1 = float(input("Digite o um valor: "))
print("\n")

#Calculo convesão para centimetros
centimetros = n1*100
print(f'{n1:.2f} metros convertidos, equivale a: {centimetros:.0f} centimetros')

#Calculo convesão para milimetros
milimetros = n1*1000
print("{:.2f} metros convertidos, equivale a: {:.0f} milimetros ".format(n1,milimetros))


