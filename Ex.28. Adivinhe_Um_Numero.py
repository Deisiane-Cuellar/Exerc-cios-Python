'''
- Escreva um programa que faça o computador pensar em um número inteiro de 0 a 5.
- Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
- O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''

from random import randint

adivinhar_numero = int(input("Adivinhe o número que estou pensando de 0 a 5:\n"))
computador = randint (0,5)


if adivinhar_numero == computador:
    print("Parabéns, você acertou\n")
else:
    print("Não foi dessa vez!!\n")

print("\nO Número que pensei foi: ", computador)