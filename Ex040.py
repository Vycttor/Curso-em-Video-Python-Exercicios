#Ex .40 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.

#-Média abaixo de 5.0: REPROVADO.
#-Média entre 5.0 e 6.9: RECUPERAÇÃO.
#-Média 7.0 ou superior: APROVADO.

#Código feito dia 31/10/2024.
#Feito upgrade nas condições dia 04/11/2024.

#Esse bloco de código solicita usuário forcer informações para analise.
print('=='*15)
Nome_aluno = str(input('Informe o nome do aluno: '))
nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))
print('=='*25)

#Bloco, realiza calculo da média.
media = (nota_1+nota_2)/2

#Bloco, usa condição para realiazar analises, conforme regras.
if media < 5:
    print(f'A média do aluno(a) {Nome_aluno} é {media:.2f}, está REPROVADO.')
    print('=='*25)
elif media >= 7.00:
    print(f'A média do aluno(a) {Nome_aluno} é {media:.2f}, está APROVADO.')
    print('=='*25)
elif media >= 5 and 6.9:
    print(f'A média do aluno(a) {Nome_aluno} é {media:.2f}, está de RECUPERAÇÃO.')
    print('=='*25)
