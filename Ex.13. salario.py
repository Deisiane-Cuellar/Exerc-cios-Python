'''Exercício Python 013: 
-Faça um algoritmo que leia o salário de um funcionário;
-Mostre seu novo salário, com 15% de aumento.'''

salario = float(input("Digite seu salário atual: R$ "))
aumento = (15*salario)/100
salario_aumento = (salario + aumento)

print("O Seu salário com 15% de aumento será: {:.2f}".format(salario_aumento))



