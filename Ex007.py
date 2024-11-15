# Ex 007 Desenvolva um programa que leia as duas notas de um aluno, 
# calcue e mostre sua media.

print("PROGRAMA CALCULA A MÉDIA DO ALUNO")
print("\n")
#Solicita para o usuario informar as duas notas do aluno.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
print("\n")

#Calculo média do aluno.
soma = nota1+nota2
media = (nota1+nota2)/2
print("A soma das notas {:.2f} e {:.2f} =: {:.2f} ".format(nota1,nota2,soma))
print("A média do aluno é =: {} ".format(media))