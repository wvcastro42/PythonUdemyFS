from math import trunc
num = int(input('Digite um número inteiro menor que 9999: '))

if num > 9999:
    while num > 9999:
        num = int(input('Digite um número intero menor que 9999: '))

un = ((num // 1) % 10)
dz = ((num // 10) % 10)
cen = ((num // 100) % 10)
mil = ((num // 1000) % 10)

print('unidade: {}'.format(un))
print('dezena: {}'.format(dz))
print('centena: {}'.format(cen))
print('milhares: {}'.format(mil))
