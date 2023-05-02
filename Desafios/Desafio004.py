var01 = input("Digite algo: ")
print(f"É do tipo: {type(var01)},\n Contém APENAS letras? {var01.isalpha()}\n Faz parte do código ASCII? {var01.isascii()} \n Contém APENAS números? {var01.isnumeric()} \n Contém APENAS caracteres Minúsculos? {var01.islower()} \n Contém APENAS caracteres maiúsculos? {var01.isupper()} ")
