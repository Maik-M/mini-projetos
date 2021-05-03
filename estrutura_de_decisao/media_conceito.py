# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#
# Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
#
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def imprime_nome(nome):
    [print(i, end=' ') for i in nome]


def calcula_media(nota_1, nota_2):
    return (nota_1 + nota_2) / 2


finalizador = 1
print('CALCULA MÉDIA - CONCEITO -----------------------------------------------------------------')
while finalizador == 1:
    aluno = input('Digite o nome e sobrenome do(a) Aluno(a): ').split(' ')
    nota_1 = 0
    nota_2 = 0
    temp = 1
    while temp == 1:
        nota_1 = float(input('Digite a primeira nota: '))
        nota_2 = float(input('Digite a segunda nota: '))
        if (nota_1 > 10) or (nota_2 > 10):
            print(90 * '-' + '\n'
                             'AS NOTAS PRECISAM SER MENORES QUE 10!')
        else:
            temp = 0

    media = calcula_media(nota_1, nota_2)
    conceito = ''
    situacao = ''

    if media < 6:
        situacao = 'REPROVADO!'
        if media < 4:
            conceito = 'E'
        else:
            conceito = 'D'
    else:
        situacao = 'APROVADO!'
        if (media >= 6) and (media < 7.5):
            conceito = 'C'
        elif (media >= 7.5) and (media < 9):
            conceito = 'B'
        elif media >= 9:
            conceito = 'A'

    print(90 * '-')
    print('Aluno(a):', end=' ')
    imprime_nome(aluno)
    print(f'\nNota 1          : {nota_1}\n'
          f'Nota 2          : {nota_2}\n'
          f'Média           : {round(media, 2)}\n'
          f'Conceito        : {conceito}\n'
          f'Situação        : {situacao}')
    print(90 * '-')

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
print(40 * '-' + 'FINALIZANDO' + 40 * '-')



