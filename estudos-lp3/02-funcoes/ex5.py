def palindromo():

    palavra = list(input('Digite uma palavra: '))

    if palavra == list(reversed(palavra)):
        print('É um palíndrmo!')
    else:
        print('Não é um palíndromo.')

palindromo()