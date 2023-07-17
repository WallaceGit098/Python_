soma = 0
for cont in range(0, 6):
    numero = int(input("Digite um Número: "))
    if numero % 2 == 0:
        soma += numero
print(f"A soma de todos os Números PARES é {soma}!")
