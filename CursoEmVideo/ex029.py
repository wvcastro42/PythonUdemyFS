velocidade = 0
while velocidade <= 80:
    velocidade = float(input('Digite a velocidade do carro: '))
    if velocidade > 80:
        print('Você foi multado!')
        print('A multa é no valor de R$ {:.2f}'.format((velocidade - 80) * 7))
