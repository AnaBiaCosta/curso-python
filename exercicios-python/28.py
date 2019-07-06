import random
pc_num = random.randint(1,5)

user_num = int(input('Digite um número entre 1 e 5:'))


if pc_num == user_num:
    print('Você ganhou!')
else:
    print('Você perdeu...')

