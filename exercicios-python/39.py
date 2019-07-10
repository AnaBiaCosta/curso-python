anoNasc = int(input('Ano de Nascimento:'))


idade = 2019 - anoNasc



if idade < 18:
    print('{}AINDA VAI SE ALISTAR \n'
        'Você tem {} anos e ainda faltam {} anos para o seu alistamento.'. format('\033[33m', idade, (18-idade)))

elif idade == 18:
    print('{}HORA DE SE ALISTAR'.format('\033[32m'))

else:
    print('{}PASSOU DO TEMPO \n'
          'Você tem {} anos e já passaram {} anos do seu alistamento.'.format('\033[31m', idade, (idade - 18)))
