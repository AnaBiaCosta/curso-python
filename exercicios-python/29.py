velocidade = int(input('Velocidade atual: '))

if velocidade <= 80:
    print('Você está dentro da velocidade permitida')

else:
    excesso = velocidade - 80
    multa = excesso * 7

    print('Você está {}km acima da velocidade permitida. Sua multa é de R${:.2f}'.format(excesso, multa))
    