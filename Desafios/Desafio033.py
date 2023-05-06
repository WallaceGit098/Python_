num_01 = int(input("Digite um número: "))
num_02 = int(input("Digite outro número: "))
num_03 = int(input("Digite mais um número: "))
menor = num_01
maior = num_01

if num_02 < menor and num_02 < num_03:
    menor = num_02
if num_03 < menor and num_03 < num_02:
    menor = num_03

if num_02 > maior and num_03 < num_02:
    maior = num_02
if num_03 > maior and num_02 < num_03:
    maior = num_03

print(f"O menor número é o {menor}")
print(f"O maior número é o {maior}")
