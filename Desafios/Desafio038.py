num_01 = int(input("Digite um Número: "))
num_02 = int(input("Digite outro Número: "))

if num_01 > num_02:
    print(f"O {num_01} é MAIOR que {num_02}!!")
elif num_02 > num_01:
    print(f"O número {num_02} é MAIOR que {num_01}!!")
else:
    print("Não existe número maior, os 2 números são IGUAIS")