#Ex 012 Faça um algoritimo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

#Função realiza o calco de aplicação do desconto de 5% sobre o produto.
def desconto(produto):
    descont = 5
    valor_descont = (produto*descont)/100
    print("O Valor de {} % de desconto sobre o produto é de R$ {:.2f} reais".format(descont,valor_descont))
    novo_preco_produto = produto - valor_descont
    print("O Valor do praduto com desconto é de R$ {:.2f} reais".format(novo_preco_produto))

#Solicita para o usuario fornecer o valor do produto desejado.
produto = float(input("Digite o valor do produto: R$ "))
print("\n")

#Chama/invoca a função desconto.
desconto(produto)
