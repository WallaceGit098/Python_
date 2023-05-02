salario_atual = float(input("Digite o salário atual: "))

aumento = (salario_atual/100)*15
salario_reajustado = salario_atual + aumento
print(f"O salário do funcionário após o reajuste é R${salario_reajustado:.2f}")