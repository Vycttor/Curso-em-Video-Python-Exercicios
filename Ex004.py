#EX004 Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo
# e todas as informações possíveis sobre ele.

#Programa tem como objetivo verificar o tipo do valor.
print("PROGRAMA VERICA O TIPO DO VALOR INFORMADO\n")
n = input("Digite um valor: ")
print('\n')

#Mostra na tela os tipo do valor informado pelo usuario.
print("isnumeric")
print("Verifica se é numerico: ",n.isnumeric())
print("\n")
print("isupper")
print("Verificar se são letras maiuscula: ",n.isupper())
print("\n")
print("islower")
print("Verifica se são letra minusculas: ",n.islower())
print("\n")
print("isalnum")
print("Verifica se uma string contém apenas caracteres alfanuméricos, ou seja, letras e números: ",n.isalnum())
print("\n")
print("isalpha")
print("Verifica se uma string contém apenas caracteres alfabéticos, ou seja, letras maiúsculas (A-Z) e minúsculas (a-z): ",n.isalpha())
print("\n")
print("isascii")
print("Verifica se um caractere pode ser representado como um caractere US-ASCII de 7–bit válido: ",n.isascii())
print("\n")
print("isdecimal")
print("Retorna um valor booleano, verdadeiro ou falso,\n dependendo se a string de entrada contém todos os caracteres decimais: ",n.isdecimal())
print("\n")
print("isdigit")
print("Verifica se todos os elementos de uma string são dígitos: ",n.isdigit())
print("\n")
print("isidentifier")
print("Verifica se uma string é um identificador válido, retornando True se for e False se não for: ",n.isidentifier())
print("\n")
print("isprintable")
print("Verifica se todos os caracteres de uma string são imprimíveis,\n retornando True se for o caso, ou False caso contrário: ",n.isprintable())
print("\n")
print("istitle")
print("Verifica se uma string está no formato de título, ou seja, se a primeira letra de cada palavra está em maiúscula: ",n.istitle())
