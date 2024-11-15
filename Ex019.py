#Ex019 Um professor quer sortear um dos seu quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

#Foi importado o modolo random para trabalhar com sorteio.
import random

#Solcita apara a o usuario colocar o nome dos quatros  alunos
nome1 = str(input("Digite o neme do aluno: "))
nome2 = str(input("Digite o neme do aluno: "))
nome3 = str(input("Digite o neme do aluno: "))
nome4 = str(input("Digite o neme do aluno: "))

#Array com 3 posições, recebe os nomemes para o sorteio do nome do aluno escolhido.
lista = [nome1,nome2,nome3,nome4] 

#Mostra na tela, o nome do aluno escolhido, com o uso do random.choice.
print('{}, foi escolhido para apagar o quadro hoje. '.format(random.choice(lista)))

