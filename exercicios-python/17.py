co = int(input('Cateto oposto:'))
ca = int(input('Cateto adjacente:'))

sc = co*2 + ca*2
h = sc**(1/2)

print('O valor dá hipotenusa é {:.2f}'.format(h))