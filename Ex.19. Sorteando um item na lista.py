'''Exercício Python 019: 
- Sortear um dos seus quatro alunos para apagar o quadro.
- Faça um programa que leia o nome dos alunos;
- Escreva na tela o nome do escolhido.'''

import random

aluno_01 = input("Digite o nome do 1º Aluno: ")
aluno_02 = input("Digite o nome do 2º Aluno: ")
aluno_03 = input("Digite o nome do 3º Aluno: ")
aluno_04 = input("Digite o nome do 4º Aluno: ")

lista = [aluno_01, aluno_02, aluno_03, aluno_04]
aluno_escolhido = random.choice(lista)

print("O aluno escolhido foi: {}".format(aluno_escolhido))

