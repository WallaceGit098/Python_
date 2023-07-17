primeiro = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a Razão? "))
decimo = primeiro + (10 -1) * razao
for cont in range(primeiro,decimo + razao, razao):
    print(cont, end="=>")

