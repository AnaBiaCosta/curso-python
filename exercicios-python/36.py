casa = float(input('Valor da casa: R$'))
salario = float(input('Valor do salário: R$'))
anos = int(input('Quantos anos pretende financiar:'))


qtnanos = anos * 12
prestacao = casa / qtnanos
porcentagemsalario = salario*0.3

if prestacao > porcentagemsalario:
    print('\033[1;31mA prestação da casa ficou em R${:.2f} \n'
          'Infelizmente seu empréstimo foi NEGADO \n'
          'Você não pode comprometer mais do que R${:.2f} do seu' 
          ' salário'.format(prestacao, porcentagemsalario))
else:
    print('\033[1;32mA prestação da casa ficou em R${:.2f}\n'
          'Empréstimo CONCEDIDO'.format(prestacao))