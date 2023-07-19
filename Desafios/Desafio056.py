
idade_total = 0
nome_velho = 0
velho = 0
mulher_20 = 0

for i in range(1,5):
    nome = str(input("Qual o Primeiro Nome da Pessoa? "))
    idade = int(input("Qual a Idade? "))
    sexo = str(input("Qual o Sexo da Pessoa? [M/F] ")).upper()
    idade_total += idade
    if sexo == "M" and i == 1:
        velho = idade
        nome_velho = nome
    elif sexo == "M" and idade > velho:
            nome_velho = nome
            velho = idade
    elif sexo =="F" and idade < 20:
         mulher_20 +=1
         
    
media = (idade_total)/4

print(f"""O Homem mais velho é o {nome_velho} que tem {velho} anos!
A média de idade do grupo é {media} Anos!
No grupo existem {mulher_20} Mulheres com MENOS de 20 anos!""")


        
