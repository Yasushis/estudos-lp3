def contarLetras(frase):

    vogais = ('a', 'e', 'i', 'o', 'u', 'á', 'à', 'â', 'ã', 'é', 'ê', 'õ', 'ó', 'ú', 'í', 'ô')
    consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'q', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ç')
    
    consoante = 0
    vogal = 0

    for letra in frase:

        if letra in vogais:
            vogal += 1
        elif letra in consoantes:
            consoante += 1
    
    print(f'Consoantes: {consoante}')
    print(f'Vogais: {vogal}')


frase = input('Escreva uma frase: ').lower()

contarLetras(frase)