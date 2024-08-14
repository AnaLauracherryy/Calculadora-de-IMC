velocidade = float(input('Qual é sua velocidade?'))
if velocidade <= 80:
    print('Ok, sem problemas')
else:
    print('Você será multado!!!')
    qtdemulta = velocidade - 80.0
    valormulta = 7.0 * qtdemulta
    print("Você pagará R${:.2f}".format(valormulta))

print('Fim do programa')
