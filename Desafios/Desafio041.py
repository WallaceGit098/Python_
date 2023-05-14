from datetime import date
ano_atual = date.today().year
nascimento = int(input("Em que ano o atleta nasceu?"))

idade = ano_atual - nascimento

if idade <= 9:
    print(f"O atleta tem {idade} anos e compete na categoria MIRIM!")
elif 14 >= idade:
    print(f"O atleta tem {idade} anos e compete na categoria INFANTIL!")
elif 19 >= idade:
    print(f"O atleta tem {idade} anos e compete na categoria JUNIOR!")
elif 25 >= idade:
    print(f"O atleta tem {idade} anos e compete na categoria SÊNIOR!")
elif idade > 25:
    print(f"O atleta tem {idade} anos e compete na categoria MASTER!")
