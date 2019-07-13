# frase = 'Curso em vídeo python'
# print(frase[::2])
# print(frase.count('í'))
# print(frase.upper().count('O'))


# nome = str(input('Nome:'))

# if nome == 'Bia':
#     print('Você é muito linda!')
# print('Prazer em te conhecer {}!'.format(nome))




nome = str(input('Nome:'))
n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))
m = (n1+n2)/2

if m <= 5:
    print('{}, sua média foi {} e você foi reprovada(o) #partiufazerdenovo'.format(nome, m))
else:
    print('{}, sua média foi {} e você foi aprovada(o)! #partiuférias'.format(nome, m))
print('')
print('Consulta finalizada com sucesso!')
