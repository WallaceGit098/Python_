valor_casa = float(input("Qual o valor da Casa? "))
salario = float(input("Qual o seu Salário? "))
tempo = int(input("Em Quantos anos deseja pagar? "))

tempo_meses = tempo * 12
valor_parcela = valor_casa / tempo_meses
porcentagem_salario = (salario / 100)*30

if valor_parcela >= porcentagem_salario:
    print(f"O financiamento não pode ser aprovado devido ao valor da parcela ser alto de mais!")

else:
    print(f" Parabéns!!!\n O financiamento foi aprovado!!\n O valor da sua parcela é de: R${valor_parcela:.2f}")
