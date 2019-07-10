import random

lista = ['Pedra', 'Papel', 'Tesoura']
c = random.choice(lista)


nome = input('Qual seu nome?')
print('Olá, {}! Prepare-se, porque o jogo já vai começar! \n'.format(nome))


print('SUAS OPÇÕES \n'
      '[ 0 ] Pedra \n'
      '[ 1 ] Papel \n'
      '[ 2 ] Tesoura \n')

j = int(input('Qual sua escolha?'))


print('*.' *10)
print('Computador jogou {} \n {} jogou {}'.format(c, nome, j))
print('*.' *10)



if c == 0 and j == 0:
    print('EMPATE')

elif c == 0 and j == 1:
    print('COMPUTADOR VENCE')

elif c == 0 and j == 2:
    print('COMPUTADOR VENCE')

elif c == 1 and j == 0:
    print('{} VENCE'.format(nome.upper()))

elif c == 1 and j == 1:
    print('EMPATE')

elif c == 1 and j == 2:
    print('{} VENCE'.format(nome.upper()))

elif c == 2 and j == 0:
    print('{} VENCE'.format(nome.upper()))

elif c == 2 and j == 1:
    print('COMPUTADOR VENCE')

elif c == 2 and j == 2:
    print('EMPATE')










