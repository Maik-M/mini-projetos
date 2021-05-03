# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n = int(input('Digite um número inteiro: '))
if n < 0:
    print(f'{n} é um número negativo.')
elif n == 0:
    print(f'{n} é um número neutro.')
else:
    print(f'{n} é um número positivo.')
