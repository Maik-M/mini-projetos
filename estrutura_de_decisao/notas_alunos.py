# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
# por aluno e apresentar:
#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez.
finalizador = 1
print('CALCULA MÉDIA -------------------------')
while finalizador == 1:
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))

    media = ((nota_1 + nota_2) / 2)
    if (media >= 7) and (media <= 10):
        print('APROVADO!')
    elif media < 7:
        print('REPROVADO!')
    elif media == 10:
        print('APROVADO COM DISTINÇÃO!')

    finalizador = int(input('Deseja calcular outra média? \n'
                            '1 - Sim \n'
                            '0 - Não \n'
                            'DIGITE O NÚMERO DA OPÇÃO DESEJADA: '))
print(30 * '-' + 'FINALIZANDO' + 30 * '-')
