dias = int(input("Por quantos dias o carro foi alugado? "))
distancia = float(input("Quantos KM foram percorridos? "))

valor_dia = 60
valor_km = 0.15

valor_total_dia = valor_dia * dias
valor_total_km = valor_km * distancia

valor_total_gasto = valor_total_km + valor_total_dia

print(f"O valor total do aluguel é de R${valor_total_gasto:.2f}!")

#Melhorando o Código

print(f"O valor total do aluguel é de R${(dias * valor_dia)+(distancia * valor_km):.2f}!")