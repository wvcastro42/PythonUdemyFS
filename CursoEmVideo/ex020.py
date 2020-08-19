from random import shuffle

list_alunos = []

def my_shuffle_list(array):
    shuffle(array)
    return array

for i in range(4):
    list_alunos.append(input('Digite o nome do aluno {}: '.format(i + 1)))

print('A lista original é {}'.format(list_alunos))

print(my_shuffle_list(list_alunos))
