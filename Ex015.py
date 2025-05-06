# Ex015 Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
# o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$ 60 por dia e R$ 0,15 por km rodado.

#Variáveis Globais
preco_por_dia = 60
km_rodado = 0.15
    
print("""PROGRAMA CALCULA VALOR A SER PAGO PELO ALUGUEL DO CARRO
      """)

km = float(input("Informe quantos km foi rodado com o carro: "))
dias = int(input("Informe a quantidade de dias que o carro foi alugado: "))
print("\n")

#Formula: calculate the following variables.
precoAluguel = (km*km_rodado) + (dias*preco_por_dia)
print(f'Preço do  {km} Km rodado R$ {km*km_rodado:.2f}')
print(f'Preço do {dias} dias locados R$ {dias*preco_por_dia}')

print("O valor total a ser pago pelo alugue do carro é de R$ {:.2f} reais ".format(precoAluguel))

