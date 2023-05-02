valor_prod = float(input("Digite o valor do produto: "))
desconto = (valor_prod/100)*5
valor_final = valor_prod - desconto


print(f"O valor do produto em oferta é R${valor_final:.2f}!!")