# Ex013 Faça um algoritimo que leia o sálario de um funcionário e mostre
# seu novo sálario, com 15% de aumento.

#Função para aumento do salário
def aumento(salario):
    aumento_15 = 15
    valor_do_aumento = (salario*aumento_15)/100
    print("O valor do aumento de {} %, sobre o salário é  de R$ {:.2f} reais".format(aumento_15,valor_do_aumento))
    novo_salario = salario+valor_do_aumento
    print("Aumento: R$ {:.2f} reais + salário de R$ {:.2f} reais, novo salário passar a ser R$ {:.2f} reais ".format(valor_do_aumento,salario,novo_salario))

print("PROGRAMA CALCULA O AUMENTO DE 15% DO SALÁRIO")
print("\n")
#Linha abaixo solicita para o usuario informar o salário.
salario = float(input("Digite o valor do salário: "))
print("\n")

#Chama/invoca função que calcula aumento do salario
aumento(salario)
