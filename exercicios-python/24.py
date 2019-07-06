nome = input('Nome da cidade:')
separar = nome.split()
primeiro = separar[0]

print('Começa com Santo: {}'.format('Santo' in primeiro))