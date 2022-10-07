#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# R$0,45 para viagens mais longas.

viagem = int(input("Informe a distância da viagem (Km): "))

valor_limite = (0.50*viagem)
viagem_longa = (0.45*viagem)

if viagem <= 200:
    print("O valor da sua passagem será: R$ {}.".format(valor_limite))
elif viagem > 200:
    print("O Valor da sua passagem será: R$ {}.".format(viagem_longa))