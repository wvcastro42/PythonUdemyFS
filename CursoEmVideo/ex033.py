num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

print('Menor número: {}'.format(num1 if (num1 < num2 and num1 < num3) else num2 if (num2 < num1 and num2) < num3 else num3))

print('Maior número: {}'.format( num1 if (num1 > num2 and num1 > num3) else num2 if (num2 > num3 and num2 > num1) else num3))
