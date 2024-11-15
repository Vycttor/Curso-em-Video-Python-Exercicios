# Ex014 Escreva um programa que converta uma temperatura digitada em
# graus ºC em ºF. A férmula para esta converção é:

#   F = 9 x C + 32
#       ------
#         5

# Função converte graus celsius em Fiefahrenheit
def convertf(c):
    b = (c*9)/5
    fiefah = b + 32
    print("{:.0f}º graus ceslsius convertiro para Fiefahrenheit é {:.0f}º Fiefahrenheits".format(c,fiefah))

print("PROGRAMA CONVERTE GRAUS CELSIUS EM FIEFAHRENHEIT\n")
c = int(input("Digite a temperatura em graus celsius: "))
print("\n")

#Chama/invoca a funçao para conversão
convertf(c)