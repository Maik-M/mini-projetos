# 5 - Faça um Programa que converta metros para centímetros.
opcao = 1
print('CONVERTER METROS PARA CENTIMETROS')
while opcao == 1:
    medida = float(input('Digite a medida: '))

    resultado = medida / 100
    print(f'{medida}m são {resultado}cm')
    print('Deseja continuar convertendo? \n'
          '1 - Sim \n'
          '0 - Não')
    opcao = int(input())

print(30 * '-' + 'FINALIZANDO' + 30 * '-')

