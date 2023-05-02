frase = str(input("Digite uma frase: ")).upper()

contar = frase.count("A")
encontra_primeira = frase.find("A")
encontra_ultima = frase.rfind("A")
print(f" A letra 'A' aparece {contar} vezes na frase \n A letra 'A' aparece pela primeira vez na posição: {encontra_primeira}\n A ultima vez que a letra 'A' aparece é na posição: {encontra_ultima}")