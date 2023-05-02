from math import hypot

cateto_op = float(input("Digite o valor do Cateto Oposto: "))
cateto_adj = float(input("Digite o valor do Cateto Adjacente: "))

print(f"O valor da Hipotenusa é de {hypot(cateto_op , cateto_adj)}!")
