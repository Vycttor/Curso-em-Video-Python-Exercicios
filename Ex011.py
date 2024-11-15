# Ex 011 Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que
# cada litro de tinta, pinta uma área de 2m².

print("PROGRAMA CALCULA A QUANTIDA DE TINTA PARA PINTAR UMA AREA\n")
print("\n")
#Solicita para o usuario, fornecer as informações necessárias.
largura = float(input("Infome a largura: "))
altura = float(input("Informe a altura: "))
print("\n")

#Calculo da area. Calculo foi corigido.
area = largura*altura
print("{:.2f} largura X 2{:.2f} altura é igual a área de {:.2f} m²".format(largura,altura,area))
tinta = area/2 
print("Será necessário {:.2f} litros de tinta".format(tinta))
