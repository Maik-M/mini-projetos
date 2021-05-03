letra = input('Digite um letra: ')
vogais = ['a', 'e', 'i', 'o', 'u']

if letra.lower() in vogais:
    print(f'"{letra}" é uma vogal.')
else:
    print(f'"{letra}" é uma consoante.')
