distância = float(input('Digite a distância em Km: '))
print('O valor da passagem será de R$ {:.2f}'.format((distância * 0.5) if (distância <= 200) else (distância * 0.45)))
