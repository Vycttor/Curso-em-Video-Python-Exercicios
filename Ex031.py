# Ex.31 Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

#Código feito dia 23/10/2024

#Função calcula o valor da viagem a ser pago, conforma a distância.
def calculo_viagem(km):
    viagem_curta = km * 0.50
    viagem_longa = km * 0.45
    if km <= 200:
        print('Para distância de {} km, o preço da passagem é de R$ {:.2f} reais '.format(km,viagem_curta))
    else:
         print('Para distância de {} km, o preço da passagem é de R$ {:.2f} reais '.format(km,viagem_longa))    

#Solicita para o usuario, informar a distância da viagem.
km = int(input('Informe a distáncia da viagem: km '))

#Chama/Invoca a função, para calcular o preço da distância da viagem.
calculo_viagem(km)