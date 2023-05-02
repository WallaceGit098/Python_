nome = input("Qual seu nome Completo? ")
nome_upper = nome.upper()
nome_lower = nome.lower()
nome_s_espaços =len(nome) - nome.count(" ")
nome_separado = nome.split()


print(f" O nome Com as letras maiúsculas fica: {nome_upper}\n O nome com as letra Mínusculas fica: {nome_lower}\n A quantidade de letras do nome é: {nome_s_espaços}\n A quantidade de letras do Primeiro Nome é: {len(nome_separado[0])}")
