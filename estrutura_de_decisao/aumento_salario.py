# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes.
#
#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#     baseado no salário atual:

#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.

def imprime_nome(funcionario):
    [print(i, end=' ') for i in funcionario]


finalizador = 1
print('CALCULAR AUMENTO DE SALÁRIO ' + 30 * '-')
while finalizador == 1:
    nome = input('Qual o nome e sobrenome do(a) funcionário(a): ').split(' ')
    print('Digite o salário de ', end='')
    imprime_nome(nome)
    print(':', end=' ')
    salario = float(input())

    aumento_20 = 20 / 100
    aumento_15 = 15 / 100
    aumento_10 = 10 / 100
    aumento_5 = 5 / 100
    salario_aumento = 0
    porcentagem = 0
    if salario <= 280:
        salario_aumento = ((aumento_20 * salario) + salario)
        porcentagem = 20
    elif (salario > 280) and (salario <= 700):
        salario_aumento = ((aumento_15 * salario) + salario)
        porcentagem = 15
    elif (salario > 700) and (salario <= 1500):
        salario_aumento = ((aumento_10 * salario) + salario)
        porcentagem = 10
    elif salario > 1500:
        salario_aumento = ((aumento_5 * salario) + salario)
        porcentagem = 5

    print('O salário de', end=' ')
    imprime_nome(nome)
    print(f'é R${salario} \nCom aumento de {porcentagem}%, o salário irá para: R${round(salario_aumento, 2)} \n'
          f'O salário aumentou R${round(salario_aumento - salario, 2)}')

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
            print('ERRO - CAMPO VAZIO!')
print(30 * '-' + 'FINALIZANDO' + 30 * '-')
