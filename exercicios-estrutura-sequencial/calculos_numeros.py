# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     o produto do dobro do primeiro com metade do segundo .
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo.
finalizar = 1
print('CALCULO DE NUMEROS')
while finalizar == 1:
    inteiros = input('Digite dois números Inteiros: ').split(' ')
    real = float(input('Digite um número Real: '))

    print(30 * '-' + 'CALCULANDO' + 30 * '-')
    a = ((int(inteiros[0]) * 2) * (int(inteiros[1]) / 2))
    b = ((int(inteiros[0]) * 3) + real)
    c = pow(real, 3)

    print(f'O produto do dobro de {inteiros[0]} com metade de {inteiros[1]} é: {a} \n'
          f'A soma do triplo de {inteiros[0]} com {real} é: {b} \n'
          f'{real} elevado ao cubo é: {c}')
    finalizar = int(input('Deseja fazer novamente? \n'
                          '1 - Sim \n'
                          '0 - Não \n'
                          'Digite o número da opção desejada: '))
print(30 * '-' + 'FINALIZANDO' + 30 * '-')
