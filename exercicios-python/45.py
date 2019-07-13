import random
lista = [0, 1, 2]
computador = random.choice(lista)


nome = input('Qual seu nome?')
print('Olá, {}! Prepare-se porque o jogo já vai começar! \n'.format(nome))



print('{}SUAS OPÇÕES:{} \n'
      '[ 0 ] {}Pedra{} \n'
      '[ 1 ] {}Papel{} \n'
      '[ 2 ] {}Tesoura{} \n'.format('\033[1m', '\033[m', '\033[31m', '\033[m', '\033[34m', '\033[m', '\033[32m', '\033[m'))

jogador = int(input('Qual sua escolha?'))

print('\n\n JO - KEN - PÔ \n\n')



#JOGO EMPATADO
if computador == 0 and jogador == 0:
    print('*.' *10)
    print('Computador jogou {}Pedra{} \n'
          '{} jogou {}Pedra{}'.format('\033[31m', '\033[m', nome, '\033[31m', '\033[m'))
    print('*.' *10)
    print('\n JOGO EMPATADO')


elif computador == 1 and jogador == 1:
    print('*.' *10)
    print('Computador jogou {}Papel{} \n'
          '{} jogou {}Papel{}'.format('\033[34m', '\033[m', nome, '\033[34m', '\033[m'))
    print('*.' *10)
    print('\n JOGO EMPATADO')


elif computador == 2 and jogador == 2:
    print('*.' *10)
    print('Computador jogou {}Tesoura{} \n'
          '{} jogou {}Tesoura{}'.format('\033[32m', '\033[m', nome, '\033[32m', '\033[m'))
    print('*.' *10)
    print('\n JOGO EMPATADO')



# COMPUTADOR VENCEU
elif computador == 0 and jogador == 1:
    print('*.' *10)
    print('Computador jogou {}Pedra{} \n'
          '{} jogou {}Papel{}'.format('\033[31m', '\033[m', nome, '\033[34m', '\033[m'))
    print('*.' *10)
    print('\n COMPUTADOR VENCEU')


elif computador == 0 and jogador == 2:
    print('*.' *10)
    print('Computador jogou {}Pedra{} \n'
          '{} jogou {}Tesoura{}'.format('\033[31m', '\033[m', nome, '\033[32m', '\033[m'))
    print('*.' *10)
    print('\n COMPUTADOR VENCEU')


elif computador == 2 and jogador == 1:
    print('*.' *10)
    print('Computador jogou {}Tesoura{} \n'
          '{} jogou {}Papel{}'.format('\033[32m', '\033[m', nome, '\033[34m', '\033[m'))
    print('*.' *10)
    print('\n \nCOMPUTADOR VENCEU')



#JOGADOR VENCEU
elif computador == 1 and jogador == 0:
    print('*.' *10)
    print('Computador jogou {}Papel{} \n'
          '{} jogou {}Pedra{}'.format('\033[34m', '\033[m', nome, '\033[31m', '\033[m'))
    print('*.' *10)
    print('\n {} VENCEU'.format(nome))

elif computador == 1 and jogador == 2:
    print('*.' *10)
    print('Computador jogou {}Papel{} \n'
          '{} jogou {}Tesoura{}'.format('\033[34m', '\033[m', nome, '\033[32m', '\033[m'))
    print('*.' *10)
    print('\n {} VENCEU'.format(nome))

else:
    print('*.' *10)
    print('Computador jogou {}Tesoura{} \n'
          '{} jogou {}Pedra{}'.format('\033[32m', '\033[m', nome, '\033[31m', '\033[m'))
    print('*.' *10)
    print('\n {} VENCEU'.format(nome))
