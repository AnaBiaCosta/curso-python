r1 = int(input('Reta 1:'))
r2 = int(input('Reta 2:'))
r3 = int(input('Reta 3:'))


if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    if r1==r2==r3:
        print('Triângulo Equilátero')
    elif r1==r2 or r1==r3 or r2==r3:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
        
else:
    print('Esses segmentos não podem formar um triângulo')