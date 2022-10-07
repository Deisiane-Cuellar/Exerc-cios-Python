'''Exercício Python 015:
- Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado;
- Quantidade de dias pelos quais ele foi alugado. 
- Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km_percorrido = float(input("Qual a Qtd de KM percorrido na viagem: "))
dia_aluguel = int(input("Quantos dias de aluguel do carro: "))

valor_diaria = (dia_aluguel*60)
valor_km = (0.15*km_percorrido)

valor_total = (valor_diaria+valor_km)

print("Você percorreu {} km e alugou o carro por {} dias.".format(km_percorrido,dia_aluguel))
print("Total Diária(s): R$ {}".format(valor_diaria))
print("Valor Total/KM percorrido: R${}".format(valor_km))
print("O seu gasto foi de R$: {}".format(valor_total))