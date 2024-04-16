def conversorNotas(nota):

    if nota < 60:
        print('F')
    elif nota < 70:
        print('D')
    elif nota < 90:
        print('C')
    elif nota < 100:
        print('B')
    else:
        print('A')

while True:

        nota = int(input('Digite uma nota de 0 a 100: '))

        if nota < 0 or nota > 100:
            print('Nota inválida')
        else:
            break

conversorNotas(nota)