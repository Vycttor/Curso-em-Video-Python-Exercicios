#Ex002 Faça um programa que leia o nome de uma pessoa e mostre uma mesnsagem de boas vindas.


nome = input("Digite seu nome: ")
print("\n")
# Abaixo é possivel mostrar dois tipos de print diferente, onde o .format é a melhor opção.
print("É um prazer te conhcerer! ",nome)
print("É um prazer te conhecer, {} !".format(nome)) #format