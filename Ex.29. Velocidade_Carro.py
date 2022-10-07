#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7 por cada Km acima do limite

velocidade = int(input("Informe a velocidade que você estava dirigindo: "))
limite_velocidade = 80

multa = (velocidade - limite_velocidade)*7

if velocidade >80:
    print("Você foi multado, terá que pagar R$: {} de multa.".format(multa))
else:
    print("Parabéns, você andou dentro do limite permitido.")

