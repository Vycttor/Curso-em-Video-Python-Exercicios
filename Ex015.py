# Ex015 Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
# o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$ 60 por dia e R$ 0,15 por km rodado.

#Variáveis Globais
preco_por_dia = 60
km_rodado = 0.15

#Função calcula despesas a serem pagas pelo aluguel do carro.
def aluguel_precp(km,dias):
    #Fórmula calcula o preço por Km rodado pelo carro.
    preco_km = km*km_rodado
    print("Foram rodados {} Km, o valor a ser pago por Km rodado é de R$ {:.2f} reais ".format(km,preco_km))
    print("\n")
    #Fórmula calcula o preço total de dias do aluguel do carro.
    preco_t_dias = dias*preco_por_dia
    print("O carro foi alugado por {} dias, onde o valor a ser pago pelo total de dias é de R$ {:.2f} reias ".format(dias,preco_t_dias))
    print("\n")
    #Calculo de total a ser pago pelo aluguel do carro.
    total_aluguel_carro = preco_t_dias+preco_km
    print("O valor total a ser pago pelo alugue do carro é de R$ {:.2f} reais ".format(total_aluguel_carro))

    
print("PROGRAMA CALCULA VALOR A SER PAGO PELO ALUGUEL DO CARRO\n")

km = int(input("Informe quantos km foi rodado com o carro: "))
dias = int(input("Informe a quantidade de dias que o carro foi alugado: "))
print("\n")

#Chama a função para calcular o valor a ser pago pelo alugue do carro.
aluguel_precp(km,dias)
