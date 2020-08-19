import random

print('Computador pensando em um número inteiro entre 0 e 5...')

num_pc = random.randint(0, 5)

num_user = int(input('Tente adivinhar um número entre 0 e 5 que o computador escolheu: '))

if num_pc != num_user:
    print('Você errou... o Computador venceu!')
    print('Numérdo do computador: {}\nSeu número: {}'.format(num_pc, num_user))
else:
    print('Parabéns guru, você adivinhou o número!\nO número é: {}'.format(num_pc))
