numero = int(input("Digite um numero de 0 a 9999: "))
unidade = numero // 1 % 10
dezena = numero //10 %10
centena = numero // 100 %10
milhar = numero // 1000 %10

print(f" O número digitado foi: {numero}\n Unidades: {unidade}\n Dezenas: {dezena}\n Centenas: {centena}\n Milhar: {milhar}")
