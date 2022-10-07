'''Veja um exemplo prático de como calcular o descanso semanal remunerado. 
Considere o mês de outubro de 2021, que possui 23 dias úteis, 4 domingos e 1 feriado. 
Ao mesmo tempo, considera-se um trabalhador remunerado que trabalha 44 horas semanais e recebe um salário de R$1.792,29.
Nesse caso, o valor da sua hora é 1.792,29/(44h por semana * 5 semanas) = 1.792,29/220 = R$8,14. 
##  hora_trab_he:
No entanto, o valor da hora extra é de, no mínimo, 50% a mais do valor da hora normal. Assim, o preço da hora extra seria
 de R$8,14 + 50% = 8,14 + 4,07(50% do 8,14) = R$12,21
soma_he_mes: 
Agora, considere que este trabalhador fez um total de 12 horas extras no mês. O valor total seria de 12 * R$12,21 = 146,52
Por fim, basta aplicar na fórmula:

DSR = (valor total das horas extras no mês / dias úteis no mês) x domingos e feriados do mês.
DSR = (146,52 / 23) x 4 = 6,37 * 4 = 25
'''

from re import X


salario = float(input("Informe seu salário: R$ "))
dia_util = int(input("Digite a quantidade de dias úteis do mês: "))

qtd_hora_extra_100 = float(input("Digite a quantidade de Horas Extras 100%: "))
qtd_hora_extra_50 = float(input("Digite a quantidade de Horas Extras 50%: "))

feriados_domingos = int(input("Digite a quantidade de domingos e feriados do mês: "))


# Valor da hora trabalhada
salario_hora = salario / 220

#calculo HE 50%
valor_he_50 = salario_hora * 1.5
receber_he50 = valor_he_50 * qtd_hora_extra_50

#calculo HE 100%
valor_he_100 = salario_hora * 2
receber_he100 = valor_he_100 * qtd_hora_extra_100



# DSR = Descanso Semanal Remunerado

hora_trab_he = salario_hora + (salario_hora/2)
#soma HE (h) no mês * hora_trab_he
soma_he_mes = (qtd_hora_extra_100 + qtd_hora_extra_50) * hora_trab_he
#formula dsr (valor total das horas extras no mês / dias úteis no mês) x domingos e feriados do mês.
dsr = (soma_he_mes / dia_util) * feriados_domingos

#desconto INSS
inss = (salario*9)/100

# Salário Líquido
salario_total = (salario + receber_he50 + receber_he100) - inss

print(f"Você irá receber:\n- HE 50%: R$ {receber_he50:.2f} \n- HE 100%: R$ {receber_he100:.2f}\n- Salário Total: R$: {salario_total:.2f}")
print(f"- DSR: R$ {dsr:.2f}")

#setembro 20 dias uteis - 6 dom/fer
