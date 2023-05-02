valor = float(input("Digite quanto dinheiro você tem: "))
dolar = 3.27

total = valor / 3.27

print(f"O que você pode comprar em dolar é US${total:.2f}!")

#Melhorando o Código


print(f"O valor que você pode comprar em dolar é US${(valor/dolar):.2f}!")
