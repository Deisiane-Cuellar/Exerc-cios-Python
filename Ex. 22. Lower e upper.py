'''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

'''

nome = input("Informe seu Primeiro Nome: ")
sobrenome = input("Informe seu Sobrenome: ")
nomecompleto = (nome+sobrenome)
print(f"Nome com letra maíuscula: {nome.upper()} {sobrenome.upper()}")
print(f"Nome com letra minúscula: {nome.lower()}{sobrenome.lower()}")
print(f"Seu nome tem {len(nomecompleto)} letras.")
print(f"Seu primeiro tem {len(nome)} letras.")

'''

nome = input("Informe seu Nome Completo: ").strip()
sepador_nome = nome.split()

print(f"Seu primeiro nome tem {len(sepador_nome[0])}")

