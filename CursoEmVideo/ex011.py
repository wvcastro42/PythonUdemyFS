alt = float(input("Digite a altura da parede em metros: "))
larg = float(input("Digite a largura da parede em metros: "))
tamanho = alt * larg
print("A altura da parede é: {:.2f} m²".format(tamanho))
print('A quantidade de tinta necessária para pintura é de {:.2f} litro(s)'.format(tamanho / 2))
