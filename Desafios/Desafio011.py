altura = float(input("Digite a altura da parede: "))
largura = float(input("Diigte a altura da parede: "))

area =  altura * largura

quant_tinta = area /2

print(f"A área da parede é {area}m² e a quantidade necessária de tinta é {quant_tinta:.1f}L!")

#Melhorando o Código

print(f"A área da parede é {(altura*largura)}m² e a quantidade necessária de tinta é {(altura*largura)/2:.1f}L!")