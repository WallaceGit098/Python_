from random import randint

user_num = int(input("Digite um número entre 0 e 5: "))
pc_num = randint(0, 5)
if user_num == pc_num:
    print("Parabéns, Você acertou!!!")
else:
    print(f"O computador escolheu {pc_num} e Venceu!!!")
