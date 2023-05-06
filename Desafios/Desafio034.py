salario = float(input("Digite o salário: "))

if salario > 1250:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.15
print(f"O seu novo salário é R${novo_salario:.2f}!!!")