num = input('digite um número inteiro menor que 9999: ')
len_num = len(num)

a = int(num)
if a > 9999:
    while int(num) > 9999:
        num = input('digite um número inteiro menor que 9999: ')
        a = int(num)

print('unidade: {}'.format(num[len_num - 1]))
print('dezena: {}'.format(num[len_num - 2]))
print('centena: {}'.format(num[len_num - 3]))
print('milhar: {}'.format(num[len_num - 4]))
