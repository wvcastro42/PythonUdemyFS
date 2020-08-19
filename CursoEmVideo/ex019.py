from random import randrange

list_alunos = []

for i in range(4):
    list_alunos.append(input('Digite o nome do aluno {}: '.format(i+1)))

print('O aluno ' + list_alunos[randrange(len(list_alunos))] + ' foi escolhido para apagar a lousa!')
