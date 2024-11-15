#Ex020 O mesmo professor do desafio anterior quer sortear a odem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


#Imoirtado modolo random para trabalhar com sorteio.
import random

#Solcita apara a o usuario colocar o nome dos quatros  alunos
nome1 = str(input("Digite o neme do aluno: "))
nome2 = str(input("Digite o neme do aluno: "))
nome3 = str(input("Digite o neme do aluno: "))
nome4 = str(input("Digite o neme do aluno: "))
print("\n")

#Array com 3 posições, recebe os nomemes para o sorteio do nome do aluno escolhido.
lista = [nome1,nome2,nome3,nome4] 

#Mostra na tela, o nome do aluno escolhido, com o uso do random.choice.
print("Lista de Ordem de Paresentação dos Trabalhos.")
print("\n")

#Essa metodologia para resolução do exercico está incorreto, já que o metódo choice nesse caso não reolve o problema por completo.

''''
print('1º {}'.format(random.choice(lista)))
print('2º {}'.format(random.choice(lista)))
print('3º {}'.format(random.choice(lista)))
print('4º {}'.format(random.choice(lista)))
'''
#Abaixo segue o metodo certo usando o shuffle, já que esse vai embaralhar é mostrar uma ordem de apresentação.
#Metodo implementado dia 15/10/2024.
random.shuffle(lista)
print('Segue a ordem de nomes para apresentação do trabalho', lista)


