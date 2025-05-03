# Ex010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.

#Considere
#US$ 1,00 = R$ 3,27

dolar = 5.66 #Valor do dia 02/05/2025
print("PROGRAMA INFORMA QUANTOS DÓLARES VOCÊ PODE COMPRAR")
print("\n")
real_brazil = float(input("Digite quanto de dinheiro você tem: R$ "))
print("\n")

quantidade_dolar = real_brazil / dolar

print(f' Com R$ {real_brazil} você pode comprar $ {quantidade_dolar:.2f}')