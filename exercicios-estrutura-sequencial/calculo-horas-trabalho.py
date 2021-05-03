# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
opcao = 1
print('QUANTO VOCÊ GANHA POR MÊS')
while opcao == 1:
    salario_hora = float(input('Quanto você ganha por hora trabalhada? '))
    horas_trabalhadas_mes = float(input('Quantas horas você trabalha no mês? '))

    resultado = salario_hora * horas_trabalhadas_mes
    print(f'Você ganha R${resultado} por mês.')
    print('Quer fazer outro calculo? \n'
          '1 - Sim \n'
          '0 - Não')
    opcao = int(input())
print(30 * '-' + 'FINALIZANDO' + 30 * '-')
