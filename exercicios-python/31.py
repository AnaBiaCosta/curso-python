viagem = int(input('Tamanho da viagem em km:'))

if viagem <= 200:
    preco = viagem * 0.5
    print('O preço total da viagem é de R${:.2f}'.format(preco))

else:
    preco = viagem * 0.45
    print('O preço total da viagem é de R${:.2f}'.format(preco))