#Ex.36 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador em QUANTOS ANOS ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

#Código iniciado dia: 26/10/2024 | Finalizado dia: 28/10/2024 


#Solicita para o usuário informar o salário  e condições para pagamento.
print('º°º'*20)
salario = float(input('Informe o seu salário:R$ '))
valor_casa = float(input('Informe o valor da casa:R$ '))
anos_de_p_pagar = int(input('Em quantos anos você gostaria de pagar a casa: '))
print('º°º'*20)
print('\n')

#Calcula os 30% do salário do funcionário.
print('º°º'*20)
salario_30_porcento = salario*0.30
print('Seu salário é R$ {:.2f} reias'.format(salario))
print('30% do seu salário é de R$ {:.2f} reias'.format(salario_30_porcento))
print('º°º'*20)
print('\n')

#Calcula a parcela anual e mensal para pagamento da casa.
print('º°º'*20)
valor_prestacao_ano = valor_casa / anos_de_p_pagar
valor_pagamento_por_mes = valor_prestacao_ano / 12
print('Valor das parcelas anuais R${:.2f} anuais'.format(valor_prestacao_ano))
print('Valor das parcelas mensais R$ {:.2f} reais'.format(valor_pagamento_por_mes))
print('º°º'*20)
print('\n')

#Condição if, informa se o usuário ira poder comprar a casa...PENDENTE MANUTEÇÃO VARIFICAR O LOG.
print('º°º'*25)
if valor_pagamento_por_mes <= salario_30_porcento:
    print('EMPRÉSTIMO APROVADO, valor das parcelas mensais dentro dos 30%')
else:
    print('EMPRÉSTIMO REPROVADO, PARCELAS SUPERA OS 30% DO SALÁRIO PARA PAGAMENTO MENSAL.')

print('º°º'*25)