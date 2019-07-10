n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))


m = (n1 + n2)/2


if m < 5:
    print('{}REPROVADO'.format('\033[1;31m'))

elif m >= 5 and m <= 6.9:
    print('{}RECUPERAÇÃO'.format('\033[1;33m'))

else:
    print('{}APROVADO'.format('\033[1;32m'))