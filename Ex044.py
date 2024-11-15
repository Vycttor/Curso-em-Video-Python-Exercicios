'''
Ex 044 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
- À vista dinheiro/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.
'''


#Código feito dia: 03/11/2024.
#Feito upgrade no código, na condinção forma de pagameto opção 4, foi adicionado quantidade de parcelas.

#Bloco solicita para o usuário informar o preço do produto, e escolher a forma de pagameto.
print('=='*20)
preco_produto = float(input('Informe o preço do produto(s): R$ '))
print('=='*20)
print('\n')
print('=='*20)
print('ESCOLHA A FORMA DE PAGAMENTO NO MENU ABAIXO')
print('\n')
print('DIGITE 1 - À vista dinheiro/cheque: 10% de desconto.')
print('DIGITE 2 - À vista no cartão: 5% de desconto.')
print('DIGITE 3 - Em até 2x no cartão: preço normal.')
print('DIGITE 4 - 3x ou mais no cartão: 20% de juros.')
print('=='*20)
print('\n')
forma_de_pagamento = float(input('ESCOLHA A FORMA DE PAGAMENTO: Nº '))
print('=='*20)

'''
# Bloco de código contem 4 funções, para calculo das formas de pagamento.
def pgto_dinheiro_cheque_10(preco_produto):
    if forma_de_pagamento == 1:
        desconto_10 = (preco_produto*0.10)
        preco_com_desconto10 = preco_produto - desconto_10
        print(f'Seu desconto de 10%  é de R$ {desconto_10:.2f} reias')
        print(f'Valor da compra: R$ {preco_produto:.2f} reais')
        print(f'O valor para pgamento fica R$ {preco_com_desconto10:.2f} reais')
        print('=='*25)

def pgto_cartao_avista5(preco_produto):
    if forma_de_pagamento == 2:
        desconto_05 = (preco_produto*0.05)
        preco_com_desconto5 = preco_produto - desconto_05
        print(f'Seu desconto de 5%  é de R$ {desconto_05:.2f} reias')
        print(f'Valor da compra: R$ {preco_produto:.2f} reais')
        print(f'O valor para pgamento fica R$ {preco_com_desconto5:.2f} reais')
        print('=='*25)

def pgto_2vezes_cartao(preco_produto):
    if forma_de_pagamento == 3:
        vezes2_cartao = preco_produto / 2
        print(f'Não a desconto para pagamento parcelado')
        print(f'Valor da compra: R$ {preco_produto:.2f} reais')
        print(f'O valor para pgamento em 2X fica R$ {vezes2_cartao:.2f} reais')
        print('=='*25)


def vpgto_3vezes_cartao(preco_produto):
    if forma_de_pagamento == 4:
        q_parcelas = float(input('Quantas parcelas:Nº '))
        juros30_ = (preco_produto*20/100) + preco_produto 
        valor_parcelas = juros30_ / q_parcelas
        print(f'Valor da compra: R$ {preco_produto:.2f} reais')
        print(f'O valor com 20% de juros fica R$ {juros30_:.2f} reais.')
        print(f'O pagamento fica em {q_parcelas} X vezes de R$ {valor_parcelas:.2f} reias')
        print('=='*25)

pgto_dinheiro_cheque_10(preco_produto)

pgto_cartao_avista5(preco_produto)

pgto_2vezes_cartao(preco_produto)

vpgto_3vezes_cartao(preco_produto)
'''

#Bloco de código tem a condição iF, com menu para calculos das formas de pagamentos.
if forma_de_pagamento == 1:
        desconto_10 = (preco_produto*0.10)
        preco_com_desconto10 = preco_produto - desconto_10
        print(f'Seu desconto de 10%  é de R$ {desconto_10:.2f} reias')
        print(f'Valor da compra: R$ {preco_produto:.2f} reais')
        print(f'O valor para pgamento fica R$ {preco_com_desconto10:.2f} reais')
        print('=='*25) 
elif forma_de_pagamento == 2:
        desconto_05 = (preco_produto*0.05)
        preco_com_desconto5 = preco_produto - desconto_05
        print(f'Seu desconto de 5%  é de R$ {desconto_05:.2f} reias')
        print(f'Valor da compra: R$ {preco_produto:.2f} reais')
        print(f'O valor para pgamento fica R$ {preco_com_desconto5:.2f} reais')
        print('=='*25)
elif forma_de_pagamento == 3:
        vezes2_cartao = preco_produto / 2
        print(f'Não a desconto para pagamento parcelado')
        print(f'Valor da compra: R$ {preco_produto:.2f} reais')
        print(f'O valor para pgamento em 2X fica R$ {vezes2_cartao:.2f} reais')
        print('=='*25)
elif forma_de_pagamento == 4:
        q_parcelas = float(input('Quantas parcelas:Nº '))
        juros30_ = (preco_produto*20/100) + preco_produto 
        valor_parcelas = juros30_ / q_parcelas
        print(f'Valor da compra: R$ {preco_produto:.2f} reais')
        print(f'O valor com 20% de juros fica R$ {juros30_:.2f} reais.')
        print(f'O pagamento fica em {q_parcelas} X vezes de R$ {valor_parcelas:.2f} reias')
        print('=='*25)