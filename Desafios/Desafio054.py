maior = 0
menor = 0
for cont in range(0, 7):
    idade = int(input("Digite sua idade: "))
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print(f"Das 7 pessoas avaliadas {maior} já atingiram a Maior Idade! E {menor} ainda são MENORES de idade!")
