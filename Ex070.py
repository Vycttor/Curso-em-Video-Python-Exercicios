'''
Ex. 70. Crie um progrma que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

a) Qual o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000.
c) Qual é o nome do produto mais barato.

'''
soma_compra = produto_acima1000 = maior = menor = contador =0
barato = caro = ' '

while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip().upper()
    preco_produto = float(input('Informe o valor do produto:R$ '))

    #Incrementadores
    contador = contador + 1 # Contado para condição de comparação de itens mais caros e mais baratos.
    soma_compra = soma_compra + preco_produto
    
    #if preco_produto > 0: #Esse if não é cenessário, porém funciona da mesma forma.
        #soma_compra = soma_compra + preco_produto

    if preco_produto >= 1000:
        produto_acima1000 = produto_acima1000 + 1

        
    if contador == 1:
          maior = preco_produto
          caro = nome_produto
          menor = preco_produto
          barato = nome_produto
    else:
         if preco_produto > maior:
            maior = preco_produto
            caro = nome_produto
         if preco_produto < menor:
            menor = preco_produto
            barato = nome_produto
            
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Continuar:[S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print('sai do laço....')
print('\n')
print(f'Valor total da compra R$ {soma_compra:.2f} reais')
print(f'Produto acima de R$1000,00: {produto_acima1000} produto(s).')
print(f'O nome do produto mais barato: {barato} que custa R$ {menor:.2f} reais')
print(f'O nome do produto mais caro: {caro} que custa R$ {maior:.2f} reais')

