produto = int(input('Preço do produto:'))

desconto = (produto * 95) / 100

print('Você teve 5% de desconto! Seu produto sairá por R${:.2f}'. format(desconto))