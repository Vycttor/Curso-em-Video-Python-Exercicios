'''
Ex. 70. Crie um progrma que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

a) Qual o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000.
c) Qual é o nome do produto mais barato.

'''
soma_compra = produto_acima1000 = 0

while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip().upper()
    preco_produto = float(input('Informe o valor do produto:R$ '))
    
    if preco_produto > 0: 
        soma_compra = soma_compra + preco_produto
    if preco_produto >= 1000:
        produto_acima1000 = produto_acima1000 + 1
    #if preco_produto > 0:
     #   menor = nome_produto
    #else:

        

    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Continuar:[S/N] ')).strip()
    if continuar == 'n':
        break
    #print('sai do laço....')
print(f'preço do produto {soma_compra}')
print(f'Produto acima de 1000 {produto_acima1000}')