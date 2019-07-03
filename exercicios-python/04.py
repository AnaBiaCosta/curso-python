digitado = input('Digite algo')

print(type(digitado))
print('{} é uma letra {}'.format(digitado, digitado.isalpha()))
print('{} é um número {}'.format(digitado, digitado.isnumeric()))
print('{} é alfanumérico {}'.format(digitado, digitado.isalnum()))
print('{} está em letras maiusculas {}'.format(digitado, digitado.isupper()))
print('{} está em letras minúsculas {}'.format(digitado, digitado.islower()))



   