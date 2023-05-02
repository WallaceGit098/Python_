import random

aluno_1 = input("Nome do aluno 1: ")
aluno_2 = input("Nome do aluno 2: ")
aluno_3 = input("Nome do aluno 3: ")
aluno_4 = input("Nome do aluno 4: ")

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

escolhe_aluno = random.choice(lista_alunos)

print(f"O aluno escolhido foi {escolhe_aluno}!")