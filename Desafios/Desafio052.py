numero = int(input("Digite o Número: "))
confere = 0
for cont in range(1, numero+1):
    if numero % cont == 0:
        confere += 1
        print(cont ,end=" ")
if confere == 2:
    print(f"\nO Número é Primo")
else:
    print(f"\nO Número não é primo")
