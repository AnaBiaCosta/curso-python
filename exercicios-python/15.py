d = int(input('Por quantos dias o carro foi alugado:'))
km = int(input('Quantos kilometros ele rodou:'))

pd = d * 60
pkm = km * 0.15

print('Total à ser pago: R${:.2f}'.format(pd+pkm))
