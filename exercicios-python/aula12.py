nome = str(input('Qual seu nome?'))

if nome == 'Bia':
    print('Seu nome é lindo')

elif nome == 'Fernanda' or nome == 'Luis':
    print('Seu nome também é muito lindo')

elif nome in 'Marcos Mauricio Geonavanna Jennifer':
    print('Você é meu amigo')

else:
   print('Seu nome é feio')

print('Prazer em te conhecer, {}!'.format(nome))