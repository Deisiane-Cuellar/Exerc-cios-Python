'''
Exercício Python 020: O mesmo professor do desafio 019 quer:
- Sortear a ordem de apresentação de trabalhos dos alunos. 
- Faça um programa que leia o nome dos quatro alunos;
- Mostre a ordem sorteada.'''

from random import shuffle,choice

qtdAlunos = 0

while (qtdAlunos < 2):
    qtdAlunos = int(input("Informe a quantidade de 2 ou + Alunos: \n"))

listaAlunos = []

for i in range(qtdAlunos):
    nome_aluno = input("Digite o nome do aluno: ")
    listaAlunos.append(nome_aluno)

shuffle(listaAlunos)

print("Portanto, a sequência de alunos será: \n\n"+str(listaAlunos))


