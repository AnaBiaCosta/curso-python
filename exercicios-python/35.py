print('*-'*20)
print('CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO')
print('*-'*20)


r1 = float(input('Reta 1:'))
r2 = float(input('Reta 2:'))
r3 = float(input('Reta 3:'))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os seguimentos podem formar um triângulo')

else:
    print('Os seguimentos não podem formar um triângulo') 