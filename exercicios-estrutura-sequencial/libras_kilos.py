finalizador = 1
print('CONVERTER LIBRAS EM KILOS OU VICE-VERSA')
while finalizador == 1:
    opcao_converter = int(input('O que você deseja converter? \n'
                                'Libras em Kilos - Digite: 1 \n'
                                'Kilos em Libra - Digite: 2 \n'
                                'Digite sua opção: '))
    if opcao_converter == 1:
        libras = float(input('Digite o peso em Libras: '))
        kilos = libras // 2.205
        print(f'{libras}/l são: {kilos}/kg')
    else:
        kilos = float(input('Digite o peso em Kilos: '))
        libras = kilos * 2.205
        print(f'{kilos}/kg são: {libras}/l')

    finalizador = int(input('Deseja converter de novo? \n'
                            '1 - Sim \n'
                            '0 - Não \n'
                            'Digite o número da opção desejada: '))
print(30 * '-' + 'FINALIZANDO' + 30 * '-')
