ano = int(input('Ano de nascimento:'))
idade = 2019 - ano


if idade <= 9:
    print('Categoria: MIRIM')

elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')

elif idade >14 and idade <= 19:
    print('Categoria: SÊNIOR')

else:
    print('Categoria: MASTER')


