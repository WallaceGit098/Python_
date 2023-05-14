from datetime import date
print("[1] MASCULINO     [2] FEMININO")
sexo = int(input("Selecione a Opção que representa o seu SEXO:"))


if sexo == 1:
    nascimento = int(input("Em que ano você nasceu? "))
    data_atual = date.today().year
    idade = data_atual - nascimento

    if idade < 18:
        print(f"Você tem {idade} anos e ainda não precisa se alistar! Você ainda tem {18 - idade} anos até precisar se "
              f"alistar!")
    elif idade == 18:
        print(f"Você tem {idade} e tem que se alistar!!!")
    elif idade > 18:
        print(f"Você tem {idade} anos e já deveria ter se alistado!!! Você está atrasado {(idade - 18)} anos!")
elif sexo == 2:
    print("O alistamento Militar é OBRIGATÓRIO apenas para HOMENS")