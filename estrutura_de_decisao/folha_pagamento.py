# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
# do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#
#     ** Desconto do IR:
#     -- Salário Bruto até 900 (inclusive) - isento
#     -- Salário Bruto até 1500 (inclusive) - desconto de 5%
#     -- Salário Bruto até 2500 (inclusive) - desconto de 10%
#     -- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
#        dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
def calcula_salario(hora_trabalho, horas_mes):
    return hora_trabalho * horas_mes


def imprime_nome(nome):
    [print(i, end=' ') for i in nome]


finalizador = 1
print('CALCULO DE FOLHA DE PAGAMENTO ' + 50 * '-')
while finalizador == 1:
    nome = input('Qual o nome do funcionário? ').split(' ')
    h_t = float(input('Digite o valor da hora trabalhada: '))
    h_m = float(input('Digite a quantidade de horas trabalhada no mês: '))

    salario = calcula_salario(h_t, h_m)
    sindicato = (3 / 100) * salario
    fgts = (11 / 100) * salario
    inss = (10 / 100) * salario
    porcentagem = 0
    salario_liquido = 0
    if salario <= 900:
        porcentagem = 'Isento'
        salario_liquido = salario - (inss + sindicato)
    elif (salario > 900) and (salario <= 1500):
        porcentagem = 5
        desconto = (5 / 100) * salario
        salario_liquido = salario - desconto
        salario_liquido -= (inss + sindicato)
    elif (salario > 1500) and (salario <= 2500):
        porcentagem = 10
        desconto = (10 / 100) * salario
        salario_liquido = salario - desconto
        salario_liquido -= (inss + sindicato)
    elif salario > 2500:
        porcentagem = 20
        desconto = (20 / 100) * salario
        salario_liquido = salario - desconto
        salario_liquido -= (inss + sindicato)

    ir = 0
    if salario > 900:
        ir = (porcentagem / 100) * salario

    print('FOLHA DE PAGAMENTO - CONTRA CHEQUE -------------------------------------------\n'
          'Funcionário:', end=' ')
    imprime_nome(nome)
    print(f'\nSalário Bruto                   : R${round(salario, 2)}')
    print(f'(-) IR ({porcentagem}%)                    : R${round(ir, 2)}') if salario > 900 else print(f'(-) IR ({porcentagem})                 : R$0.00')
    print(f'(-) INSS (10%)                  : R${round(inss, 2)}\n'
          f'(-) Sindicato (3%)              : R${round(sindicato, 2)}\n'
          f'FGTS (11%)                      : R${round(fgts, 2)}\n'
          f'Total de Descontos              : R${round(ir + inss + sindicato, 2)}\n'
          f'Salario Liquido                 : R${round(salario_liquido, 2)}')

    temp = 1
    while temp == 1 and True:
        try:
            finalizador = int(input('Deseja calcular novamente? \n'
                                    '1 - Sim \n'
                                    '0 - Não \n'
                                    'DIGITE O NÚMERO DA OPÇÃO DESEJADA: '))
            if (finalizador != 1) and (finalizador != 0):
                print('OPÇÃO INVÁLIDA! \n'
                      'Digite uma opção válida!')
            else:
                temp = 0
        except ValueError:
            print('ERRO - CAMPO VAZIO OU INVÁLIDO!')
print(30 * '-' + 'FINALIZANDO' + 30 * '-')
