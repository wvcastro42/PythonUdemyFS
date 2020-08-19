import math
real = float(input("Digite um número real: "))
print("O número {} real e sua parte inteira é: {}".format(real, int(real)))
print(math.trunc(real)) #trunc remove a parte decimal do número
