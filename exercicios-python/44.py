valor = float(input('Preço do produto: R$'))

print('{}FORMAS DE PAGAMENTO{} \n'
      '[ 1 ] À vista dinheiro/cheque\n'
      '[ 2 ] À vista cartão de débido\n'
      '[ 3 ] 2x no cartão de crédito\n'
      '[ 4 ] 3x ou mais no cartão de crédito'
      .format('\033[1m', '\033[m'))

opcao = int(input('Forma de pagamento:'))

if opcao == 1:
    desconto = (valor * 90)/100
    print('PAGAMENTE À VISTA DINHEIRO/CHEQUE \n Com desconto de 10%, sua compra sai por R${:.2f}'.format(desconto))

elif opcao == 2:
    desconto = (valor * 95)/100
    print('PAGAMENTO À VISTA CARTÃO DE DÉBITO \n Com desconto de 5%, sua compra sai por R${:.2f}'.format(desconto))

elif opcao == 3:
    print('PARCELAMENTO EM 2X NO CARTÃO DE CRÉDITO \n Sua compra sai por R${:.2f}'.format(valor))

else:
    juros = (valor * 120)/100
    print('PARCELAMENTO EM 3X NO CARTÃO DE CRÉDITO \n Com juros de 20%, sua compra sai por R${:.2f}'.format(juros))

