'''Exercício Python 012: 
- Faça um algoritmo que leia o preço de um produto
- Mostre seu novo preço, com 5% de desconto.'''

produto = float(input("Digite o valor do produto: "))
desconto = (5*produto)/100
valor = (produto-desconto)

print("O valor do produto com 5% desconto é: R$ {:.2f}".format(valor))