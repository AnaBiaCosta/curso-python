salario = int(input('Seu salário:'))

if salario > 1250:
    aumento = (salario * 110)/100
    print('Com aumento de 10% seu salário será de R${}'.format(aumento))

else:
    aumento = (salario * 115)/100
    print('Com aumento de 15% seu salário será de R${}'.format(aumento)) 