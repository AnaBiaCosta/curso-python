import math
angulo = int(input('Ângulo:'))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print('O angulo {}, corresponde à: \n Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(angulo, sen, cos, tg))