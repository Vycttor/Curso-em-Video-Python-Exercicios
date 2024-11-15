#Ex.29 Escreva um programa que leia a velocidade de um carro.

#Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$ 7,00 por cada Km acima do limite.

#Codigo feito dia 23/10/2025

#Função calcula o valor da multa, mediante a velocidade.
def multa(velocidade_carro):
    #Calculo multa
    limite_velocidade = 80
    calculo_multa = velocidade_carro - 80
    valor_multa = calculo_multa*7
    #Condição If verifica, velociadade e aplicação de multa.
    if velocidade_carro >= 80:
        print('Sua velocidade é {} Km/h, você ultrapassou o limite de velocidade {} km/h'.format(velocidade_carro,limite_velocidade))
        print('Sua multa é de R$ {:.2f} reais'.format(valor_multa))
    else:
        print('Sua velocidade é {} Km/h'.format(velocidade_carro))    

#Solicita para o usuario, informar a velocidade do carro.
velocidade_carro = float(input('Informe a velocidade do Carro:Km/h '))

# Chama/invoca a função para calculo da multa.
multa(velocidade_carro)