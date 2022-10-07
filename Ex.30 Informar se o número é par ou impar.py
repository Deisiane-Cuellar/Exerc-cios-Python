#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

numero = int(input("Informe um número inteiro: "))
resultado = numero % 2

print("O Resto da divisão: {}".format(resultado))

if resultado == 0:
    print("O número: {} é PAR.".format(numero))
else:
    print("O número: {} é IMPAR.".formart(numero))