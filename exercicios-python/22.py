nome = input('Seu nome:')
separar = nome.split()

print('Todas as letras maiúsculas: {}'.format(nome.upper()))
print('Todas as letras minúsculas: {}'.format(nome.lower()))
print('Total de letras: {}'.format(len(nome) - nome.count(' ')))
print('Total de letras do primeiro nome: {}'.format(len(separar[0])))









