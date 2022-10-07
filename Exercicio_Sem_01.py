''' Exercício de fixação 2: 
-Elabore um algoritmo que solicite ao usuário seu ano de nascimento
-calcule sua idade com relação ao ano de 2020, sendo que o usuário já fez aniversário nesse ano.


ano_nascimento = int(input("Informe seu ano de nascimento: "))
aniversario = input("Você já fez aniversário este ano? (s/n) ").lower()
idade = 2022 - ano_nascimento
idade_n = idade - 1

if (aniversario == "s" ):
    print(f"Sua idade é: {idade}")
else:
    print(f"Sua idade é: {idade_n}") '''

'''####################################################################################################'''

''' Exercício de fixação 1:
Elabore um programa que solicite ao usuário, separadamente, seu nome e sobrenome e mostre a mensagem:
“Seu nome completo: Nome Sobrenome.”, com um espaço na junção dos nomes e um ponto no final, sem pular linha

nome = input("Informe seu NOME: ")
sobrenome = input("Informe seu SOBRENOME: ")
nomes = (nome+sobrenome)

print(f"Seu nome completo é: {nome}",f"{sobrenome}",sep='_') '''

'''####################################################################################################'''

'''Exercício de fixação 1:
- Crie um programa que pergunte a idade do usuário. 
- Caso seja maior de idade, deve mostrar uma mensagem informando que pode se inscrever para fazer o teste
para tirar a carteira de motorista.'

idade = int(input("Digite sua idade: "))

if (idade >= 18):
    print("Você pode se inscrever para o fazer o teste de CNH.")
else:
    print("Você precisa completar 18 anos para tirar a CNH")

'''
'''####################################################################################################'''

'''Exercício de fixação 1: 
 -Crie um programa que pergunte o nome do cliente para ser inserido em um cartão de crédito, com espaço
máximo de 20 caracteres.
-Caso o usuário informe um nome maior, deve mostrar uma mensagem informando que o nome é
extenso demais e deve ser abreviado.
- Dica: para saber o tamanho
de uma string, usar a função len. Exemplo: len(nome).

nome = input("Infome o nome para inserir no cartão de crédito: ")
contador = len(nome)

if (contador > 20):
    print("Você precisa abreviar o nome.")
else:
    print(f"O nome a ser impresso no cartão: {nome}")'''

'''####################################################################################################'''

''' Exercício de fixação 3: 
Crie um programa que solicite um número ao usuário e informe se é par ou ímpar. 
Dica: para saber se um número é par ou ímpar, calcular o resto da divisão desse número
por 2 (operador %). Se o resultado for 0, o número será par; se for 1, será ímpar

numero = int(input("\n\nInforme um número inteiro: "))

if (numero % 2 == 0):
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é IMPAR")'''

'''####################################################################################################'''

'''Exercício de fixação 4: 
-Crie um programa que solicite ao usuário o seu salário. 
-Se o valor for inferior a R$ 5.000, calcule um abono de fim de ano de 15%. 
-Caso contrário, o abono será de 10%. 
Informe ao usuário seu valor de abono de fim de ano.

salario = float(input("\n\nInforme seu salário: R$ "))
abono_15 = (15*salario)/100 + salario
abono_10 = (10*salario)/100 + salario

if (salario >= 5000):
    print(f"\n\nSeu salário com abono de 15% é R$ {abono_15}\n")
else:
    print(f"\n\nSeu salário com abono de 10% é R$ {abono_10}\n")'''

'''####################################################################################################'''

'''
Exercício de fixação 5: 
Crie um programa que pergunte ao usuário em que turno trabalha. Formato da entrada: M – manhã, T
– tarde ou N – noite. 
Mostre a mensagem “Bom dia!”, “Boa tarde!”, “Boa noite!” ou “Valor inválido!”, conforme o caso.


nome = input("Infome seu nome: ")
turno = input("Infome o turno que você trabalha: M – manhã, T – tarde ou N – noite: ").upper()

if (turno == 'M'):
    print(f"Bom dia {nome}!")
elif (turno == 'T'):
    print(f" Boa tarde {nome}!!")
elif (turno == 'N'):
    print(f" Boa noite {nome}!!")
else:
    print("Valor inválido")
    '''

'''####################################################################################################'''

'''Exercício de fixação 6: 
Crie um programa que solicite ao usuário dois números e a operação que deseja executar entre eles. 
Mostre o resultado dessa operação no formato: num1 op num2 = resultado.

for s in range (4):
    num1 = int(input("Informe um número: "))
    num2 = int(input("Informe um número: "))
    oper = input("Informe a operação que deseja realizar: \nSomar, Subtrair, Multiplicar, Dividir: ").upper()

    somar = (num1+num2)
    subtrair = (num1-num2)
    multiplicar = (num1*num2)
    dividir = (num1/num2)


    if (oper == 'SOMAR'):
        print (f"{num1}","+", f"{num2}","=", somar)
    elif (oper == 'SUBTRAIR'):
        print (f"{num1}","-", f"{num2}","=", subtrair)
    elif (oper == 'MULTIPLICAR'):
        print (f"{num1}","*", f"{num2}","=", multiplicar)
    elif (oper == 'DIVIDIR'):
        print (f"{num1}","/", f"{num2}","=", dividir)'''


'''####################################################################################################'''
''' Elabore um programa que solicite ao usuário seu nome e
mostre cada uma das letras do nome em uma linha diferente do console.

soma = 0
for i in range (3):
    num = int(input("Digite o " + str(i + 1) + " número: "))
    soma += num
print("A soma dos números é", soma)
'''
'''####################################################################################################'''
'''
i = int(input("inicio: "))
f = int(input("fim: "))
p = int(input("passo: "))

for c in range (i, f, p):
    print(c)
print("fim")
'''
'''####################################################################################################'''
'''
Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.


from time import sleep

for i in range (0,11):
    print(i)
    sleep(0.4)
print("Acabou")'''

'''####################################################################################################'''

'''Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''
'''

n = 1
while n != 0:
    n = int(input("Digite um número: "))
print("Fim")


r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar: ")).upper()
print("fim")'''

'''####################################################################################################'''

'''Crie um programa que solicite ao usuário as quatro notas bimestrais de uma matéria e o número de faltas.
-Informe se o aluno foi aprovado ou reprovado, bem como o motivo, a saber:
a. A média anual é 7.
b. A disciplina possui 40 aulas.
c. O mínimo exigido é 75% de presença.

nota = 0

for n in range (4):
    nota += float(input("Digite sua nota: "))

media = nota/4
print(f"Sua média é: {media:.2f}")

falta = int(input("Digite o número de faltas: "))

frequencia = 40 - (75*40)/100
print(frequencia)

if media < 7 or falta >= frequencia :
    print("Você está reprovado.")
else:
    print ("Você está aprovado")
'''

'''####################################################################################################'''
''' Elabore um programa que solicite ao usuário dez números e
efetue a multiplicação, exibindo o resultado. No entanto, se em algum momento o
número digitado for 0, deve pular esta iteração, para que o valor não seja zerado.

mult = 1
for i in range(10):
    num = int(input("Digite o " + str(i + 1) + " número: "))
    if num == 0:
        continue
    mult *= num
print("A multiplicação dos números é", mult)'''
'''####################################################################################################'''
'''
Elabore um programa que solicite ao usuário que digite indefinidamente números e efetue a soma,
 parando apenas quando o usuário digitar o
número 0'''

numero = int(input("Digite um número: "))

while numero != 0:
    numero = int(input("Digite um número: "))
        

