# Ex010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.

#Considere
#US$ 1,00 = R$ 3,27

#Função conversão
def reais_para_dolar(reais):
    um_dolar = 5.61
    pode_comprar = reais / um_dolar
    print("Com R$ {:.2f} reias você pode comprar U$ {:.2f} dólares ".format(reais,pode_comprar))

print("PROGRAMA INFORMA QUANTOS DÓLARES VOCÊ PODE COMPRAR")
print("\n")
reias = float(input("Digite quanto de dinheiro você tem: R$ "))
print("\n")

#Chama a função
reais_para_dolar(reias)