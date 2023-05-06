distancia = float(input("Digite a Distancia: "))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45
print(f"O valor gasto na viagem é de R${valor}")