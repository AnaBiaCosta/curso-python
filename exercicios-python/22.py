nome = str(input('Seu nome:')).strip()
separar_nomes = nome.split()

print('Nome em letras maiúsculas: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
print('Total de letras no nome: {}'.format(len(nome) - nome.count(' ')))
print('Total de letras no primeiro ano: {}'.format(len(separar_nomes[0]))) 
#separa em lista e depois pega o primeiro item da lista
