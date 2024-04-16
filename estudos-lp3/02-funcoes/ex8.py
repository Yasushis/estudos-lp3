from collections import Counter

def contadorFrase(frase):
    frase = frase.replace('.', '')
    frase = frase.replace(',', '')
    frase = frase.replace('?', '')
    frase = frase.replace('!', '')
    print((dict(Counter(frase.split()))))


a = input('Digite uma frase: ')
contadorFrase(a)