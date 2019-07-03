altura = int(input('Altura da parede:'))
largura = int(input('Largura da parede:'))

area = altura * largura
tinta = area / 2

print('A área total é de {:.2f} metros quadrados \n Você precisará de {:.2f} litros de tinta'.format(area, tinta))