numero = int(input("Digite o Número a ser convertido: "))
print(''' Selecione para qual base deseja converter?:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
''')
base = int(input("Digite a sua Opção: 1, 2 ou 3. "))

if base == 1:
    print(f"O número {numero} convertido para BINÁRIO é {bin(numero)[2:]}!!")
elif base == 2:
    print(f"O número {numero} convertido para base OCTAL é {oct(numero)[2:]}!!")
elif base == 3:
    print(f"O número {numero} convertido para HEXADECIMAL é {hex(numero)[2:]}!!")
else:
    print("Opção inválida!!")