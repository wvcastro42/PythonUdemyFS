num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2
print('A soma é {}, o produto é {},  a divisão é {:.3f}'.format(s, m, d), end=' >>> ') # end='algumacoisa' é para não quebrar a linha de um print para outro
print('A divisão inteira é {} e potência {}'.format(di, e))
