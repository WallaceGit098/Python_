velocidade = float(input("Digite sua velocidade: "))
limite = 80
if velocidade > limite:
    multa = (velocidade - limite) * 7
    print(f"Você foi multado em R${multa}")
else:
    print("Você não foi multado!")