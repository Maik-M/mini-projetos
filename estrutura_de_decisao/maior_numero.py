# Faça um Programa que peça dois números e imprima o maior deles.
print('MOSTRAR O MAIOR NÚMERO')
entrada = input('Digite dois números: ').split(' ')
maior = max(entrada, key=int)
print(maior)
