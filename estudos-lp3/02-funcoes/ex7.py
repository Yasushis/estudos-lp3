def forca():

    palavrasecreta = 'banana'
    auxiliar = '_' * len(palavrasecreta)
    auxiliar = list(auxiliar)
    contador = 0
    tentativas = []

    while True:

        if contador == 6:
            print('Você perdeu')
            break
        
        while True:

            tentativa = input('Digite uma letra: ')

            if len(tentativa) != 1:
                print('Digite uma letra válida')
            elif tentativa in tentativas:
                print('Essa letra já foi tentada')
            else:
                tentativas.append(tentativa)

                if tentativa in palavrasecreta:
                    for i, letra in enumerate(palavrasecreta):
                        if tentativa == letra:
                            print(letra, end='')
                            auxiliar[i] = letra
                        else:
                            print(auxiliar[i], end='')
                    print()
                    print()
                    break
                else:
                    print('Essa letra não está na palavra secreta')
                    print()
                    contador+= 1
                    break

        if '_' not in auxiliar:
            print('Você ganhou!')
            break
forca()