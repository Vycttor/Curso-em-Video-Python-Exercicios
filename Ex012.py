#Ex 012 Faça um algoritimo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

#Solicita para o usuario fornecer o valor do produto desejado.
produto = float(input("Digite o valor do produto: R$ "))
print("\n")

produto_c_desconto = produto - (produto * 0.5)

print(f'O produto custa R$ {produto} reias')
print(f'O preço do produto com desconto de 5% passa a custar R$ {produto_c_desconto:.2f}')