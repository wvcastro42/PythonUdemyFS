salário = float(input('Digite seu salário: '))
print('Seu novo salário é de R$ {:.2f}'.format(((salário + (salário * 0.1)) if salário > 1250 else (salário + (salário * 0.15)))))
