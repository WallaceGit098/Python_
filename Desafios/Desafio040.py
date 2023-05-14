nota_01 = float(input("Digite a Nota 1: "))
nota_02 = float(input("Digite a Nota 2: "))
media = (nota_01 + nota_02) / 2
if (nota_01 + nota_02) > 20.0:
    print("Digite um VALOR VÁLIDO!")
else:
    if media >= 7.0:
        print(f"O aluno teve uma Média de {media:.1f} e está APROVADO!!!")
    elif media < 5.0:
        print(f"O aluno teve uma Média de {media:.1f} e está REPROVADO!!!")
    elif 5.0 <= media <= 6.9:
        print(f"O aluno teve uma Média de {media:.1f} e está de RECUPERAÇÃO!!!")
