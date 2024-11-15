# Ex.34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

#Para salários superiores a R$1.250,00, calcule um aumento de 10%.

#Para os inferiores ou iguais, o aumento é de 15%.

#Código feito dia 23/10/24

#Função calcula, o aumento de 10 e 15 %, conforme regra estabelecida.
# //OBS: Foi implemntado o If de uma forma diferente, conforme apresentado do livro, pag78.
def cal_aumento(salario):
    if salario > 1250.00:
        aumento = salario*0.10
        novo_salario = salario+aumento
    if salario <= 1250.00:
        aumento = salario*0.15
        novo_salario = salario+aumento
    print(f'O aumento é de R${aumento:6.2f} reais, o salario reajustado é de R$ {novo_salario:6.2f} reais')        

# Solicita para o usuario , informar o salário, para calculo do aumento.
salario = float(input('Informe o salário para calculo do aumento:R$ '))

#Chama a função para, calculo do aumento.
cal_aumento(salario)
