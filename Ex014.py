# Ex014 Escreva um programa que converta uma temperatura digitada em
# graus ºC em ºF. A férmula para esta converção é:

#   F = 9 x C + 32
#       ------
#         5
print("""PROGRAMA CONVERTE GRAUS CELSIUS EM FIEFAHRENHEIT
      """)
c = int(input("Digite a temperatura em graus celsius: "))
print("\n")
#Formula to calculate Cº to Fª
fiefah = 32 + (c*9) / 5

print("{:.0f}º graus ceslsius convertiro para Fiefahrenheit é {:.0f}º Fiefahrenheits".format(c,fiefah))
