valor = 100
forma_de_pagamento = str(input("Qual a forma de pagamento? ")).upper()

if forma_de_pagamento == "DINHEIRO" or forma_de_pagamento == "CHEQUE":
    print(f"O valor do produto com 10% de desconto é de {(valor /100)* 90:.2f}")
elif forma_de_pagamento == "CARTÃO" or "CARTAO":
    parcelas = str(input("Gostaria de parcelar? ")).upper()
    if parcelas == "SIM":
        quantidade_parcelas = int(input("Em 2x ou 3x ? "))
        if quantidade_parcelas == 2:
            print(f"Parcelando em 2x o produto não tem desconto, então o valor final é de R${valor:.2f}!")
        elif quantidade_parcelas == 3:
            print(
                f"Parcelando em 3x o produto tem um acréscimo de 20%, então o valor final é de R${(valor / 100) * 120:.2f}!!")
    elif parcelas == "NÃO" or "NAO":
        print(f"À vista no cartão o produto tem um desconto de 5%, então o valor final é de R${(valor / 100) * 95:.2f}")
