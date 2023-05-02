from random import shuffle

aluno_1 = input("Nome do aluno 1: ")
aluno_2 = input("Nome do aluno 2: ")
aluno_3 = input("Nome do aluno 3: ")
aluno_4 = input("Nome do aluno 4: ")

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista_alunos)

print(f"A ordem de apresentação dos trabalhos é: {lista_alunos} ")
