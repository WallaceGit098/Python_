frase = str(input("Digite a frase: ")).split()
lista_palavras = "".join(frase)
invertido = ""
for letra in range(len(lista_palavras)-1 ,-1, -1):
    invertido += lista_palavras[letra]
if invertido == lista_palavras:
    print(f"A frase {lista_palavras}, É um PALÍNDRONO!!!")
else:
    print(f"A frase {lista_palavras}, NÃO é um PALÍNDRONO!!!!")


