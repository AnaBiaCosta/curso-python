n1 = int(input('Primeiro Número:'))
n2 = int(input('Segundo Número:'))

if n1 > n2:
    print('O {}primeiro{} valor é o maior'.format('\033[1;32m', '\033[m'))

elif n2 > n1:
    print('O {}segundo{} valor é o maior'.format('\033[1;31m', '\033[m'))

else:
    print('{}Os números são iguais'.format('\033[4;36m'))