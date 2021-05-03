# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
finalizar = 1
print('QUAL SEU PESO IDEAL? VAMOS CALCULAR!')
while finalizar == 1:
    genero = input('Você é homem ou mulher? ')
    altura = float(input('Digite a sua altura em metros: '))

    if genero.lower() == 'homem':
        peso_ideal = ((72.7 * altura) - 58)
    else:
        peso_ideal = ((62.1 * altura) - 44.7)

    print(f'Seu peso ideal seria: {peso_ideal}kg')

    finalizar = int(input('Deseja fazer novamente? \n'
                          '1 - Sim \n'
                          '0 - Não \n'
                          'Digite o número da opção desejada: '))
print(30 * '-' + 'FINALIZANDO' + 30 * '-')
