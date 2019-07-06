frase = str(input('Digite uma frase')).upper()


print('Letras A: {}'.format(frase.count('A')))
print('Primeira letra A: {}'.format(frase.find('A')+1))
print('Última letra A: {}'.format(frase.rfind('A')+1))