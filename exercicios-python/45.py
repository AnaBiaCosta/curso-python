import random
lista = [0, 1, 2]
computador = random.choice(lista)

print('{}SUAS OPÇÕES:{} \n'
      '[ 0 ] {}Pedra{} \n'
      '[ 1 ] {}Papel{} \n'
      '[ 2 ] {}Tesoura{} \n'.format('\033[1m', '\033[m', '\033[31m', '\033[m', '\033[34m', '\033[m', '\033[32m', '\033[m'))

jogador = int(input('Qual sua escolha?'))

print('\n\n JO - KEN - PÔ \n\n')



if computador == 0 and jogador == 0:
    print('*.' *10)
    print('Computador jogou {}Pedra{} \n'
          'Jogador jogou {}Pedra{} \n'.format('\033[31m', '\033[m', '\033[31m', '\033[m'))
    print('*.' *10)
    print('\n JOGO EMPATADO')


elif computador == 1 and jogador == 1:
    print('*.' *10)
    print('Computador jogou {}Papel{} \n'
          'Jogador jogou {}Papel{} \n'.format('\033[34m', '\033[m', '\033[34m', '\033[m'))
    print('*.' *10)
    print('\n JOGO EMPATADO')


elif computador == 2 and jogador == 2:
    print('*.' *10)
    print('Computador jogou {}Tesoura{} \n'
          'Jogador jogou {}Tesoura{} \n'.format('\033[32m', '\033[m', '\033[32m', '\033[m'))
    print('*.' *10)
    print('\n JOGO EMPATADO')


# COMPUTADOR VENCEU
elif computador == 0 and jogador == 1:
    print('*.' *10)
    print('Computador jogou {}Pedra{} \n'
          'Jogador jogou {}Papel{} \n'.format('\033[31m', '\033[m', '\033[34m', '\033[m'))
    print('*.' *10)
    print('\n COMPUTADOR VENCEU')


elif computador == 0 and jogador == 2:
    print('*.' *10)
    print('Computador jogou {}Pedra{} \n'
          'Jogador jogou {}Tesoura{} \n'.format('\033[31m', '\033[m', '\033[32m', '\033[m'))
    print('*.' *10)
    print('\n COMPUTADOR VENCEU')


elif computador == 2 and jogador == 1:
    print('*.' *10)
    print('Computador jogou {}Tesoura{} \n'
          'Jogador jogou {}Papel{} \n'.format('\033[32m', '\033[m', '\033[34m', '\033[m'))
    print('*.' *10)
    print('\n \nCOMPUTADOR VENCEU')



#JOGADOR VENCEU
elif computador == 1 and jogador == 0:
    print('*.' *10)
    print('Computador jogou {}Papel{} \n'
          'Jogador jogou {}Pedra{} \n'.format('\033[34m', '\033[m', '\033[31m', '\033[m'))
    print('*.' *10)
    print('\n JOGADOR VENCEU')

elif computador == 1 and jogador == 2:
    print('*.' *10)
    print('Computador jogou {}Papel{} \n'
          'Jogador jogou {}Tesoura{} \n'.format('\033[34m', '\033[m', '\033[32m', '\033[m'))
    print('*.' *10)
    print('\nJOGADOR VENCEU')

else:
    print('*.' *10)
    print('Computador jogou {}Tesoura{} \n'
          'Jogador jogou {}Pedra{} \n'.format('\033[32m', '\033[m', '\033[31m', '\033[m'))
    print('*.' *10)
    print('\n \nJOGADOR VENCEU')
