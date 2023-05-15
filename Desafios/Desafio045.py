from random import randint
itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(1, 3)
print("""
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input("Qual a sua escolha? "))
print("-="*11)
print(f"O computador jogou {itens[computador]}")
print(f"O jogador jogou {itens[jogador]}")
print("-="*11)
if computador == 0:
    if jogador == 0:
        print("O resultado é um EMPATE!")
    elif jogador == 1:
        print("O Jogador VENCEU!")
    elif jogador == 2:
        print("O computador VENCEU!")
    else:
        print("Jogada INVÁLIDA!!!")
elif computador == 1:
    if jogador == 0:
        print("O computador VENCEU!")
    elif jogador == 1:
        print("O resultado é um EMPATE!")
    elif jogador == 2:
        print("O jogador VENCEU!")
    else:
        print("Jogada INVÁLIDA!")
elif computador == 2:
    if jogador == 0:
        print("O jogador VENCEU!")
    elif jogador == 1:
        print("O computador VENCEU!")
    elif jogador == 2:
        print("O resultado é um EMPATE!")
    else:
        print("Jogada INVÁLIDA!")
