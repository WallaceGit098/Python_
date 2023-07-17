maior_peso = 0
menor_peso = 0

for p in range(1, 6):
    peso = float(input(f"O peso da {p}° é: "))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        elif peso > maior_peso:
            maior_peso = peso
print(f"O maior peso é {maior_peso}Kg!! E o menor peso é {menor_peso}Kg!!")