tamanho = float(input("Digite o tamanho em METROS: "))
centimetros = tamanho *100
milimetros = tamanho *1000

print(f"{tamanho} Metros equivalem à {centimetros:.0f} Centímetros e à {milimetros:.0f} Milímetros")

print("=" *100)
#Melhorando o Código

print(f"{tamanho} Metros equivalem à {tamanho*100:.0f} Centímetros e {tamanho*1000:.0f} Milímetros")