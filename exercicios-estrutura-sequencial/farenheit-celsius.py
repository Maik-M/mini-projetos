# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# Formula: F = (1,8.C) + 32 ------- C = (F - 32) / 1.8
finalizar = 1
print('CONVERTER GRAUS FAHRENHEIT EM GRAUS CELSIUS OU VICE-VERSA')
while finalizar == 1:
    print('O que você deseja converter? \n'
          'Fahrenheit para Celsius - Digite: 1 \n'
          'Celsius para Fahrenheit - Digite: 2')
    opcao = int(input('Qual sua opção: '))

    if opcao == 1:
        f = float(input('Digite a temperatura Fahrenheit: '))
        c = ((f - 32) / 1.8)
        print(f'{f}°F são: {c}°C')
    else:
        c = float(input('Digite a temperatura Celsius: '))
        f = ((1.8 * c) + 32)
        print(f'{c}°C são: {f}°F')

    finalizar = int(input('Deseja converter de novo? \n'
                          '1 - Sim \n'
                          '0 - Não \n'
                          'Digite o número da opção desejada: '))
print(30 * '-' + 'FINALIZANDO' + 30 * '-')
