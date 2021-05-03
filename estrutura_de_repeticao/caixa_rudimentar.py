# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar.
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador para indicar o final da compra.
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco.
# Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
# A saída deve ser conforme o exemplo abaixo:
#
#   Lojas Tabajara
#   Produto 1: R$ 2.20
#   Produto 2: R$ 5.80
#   Produto 3: R$ 0
#   Total: R$ 9.00
#   Dinheiro: R$ 20.00
#   Troco: R$ 11.00
# ...
print(45 * '-' + ' INICIANDO CAIXA ' + 45 * '-')
valor = 1
lista_produtos = {}
soma_total = 0
contador = 0
print('Por favor, digite o valor dos produtos.\n'
      'Quando não houver mais o que somar, DIGITE 0')

while valor > 0:
    try:
        valor = float(input('Valor: '))
        if valor > 0:
            contador += 1
            lista_produtos.update({'Produto ' + str(contador): valor})
            soma_total += valor
    except ValueError:
        print('Valor inválido ou vazio!')

print(95 * '-')
temp = 1
dinheiro = 0
while temp == 1:
    print(f'Total: R${round(soma_total, 2)}')
    dinheiro = float(input('Valor entregue pelo cliente: '))
    if dinheiro < soma_total:
        print('Dinheito entregue não é suficiente!\n'
              'Digite novamente ou informe ao cliente.\n')
    else:
        temp = 0
print(95 * '-')

troco = dinheiro - soma_total
for key, i in lista_produtos.items():
    print(f'{key}: R${i}')

print(f'Toral: R${round(soma_total, 2)}\n'
      f'Dinheiro entregue: R${dinheiro}\n'
      f'Troco: R${round(troco, 2)}\n' + 95 * '-')
