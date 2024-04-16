import random

def jogoAdivinhar():

    adivinhar = random.randint(1, 100)

    while True:

        palpite = int(input())

        if palpite == adivinhar:
            print('Você acertou!')
            break
        
        elif palpite < adivinhar:
            print('Valor baixo')
        
        elif palpite > adivinhar:
            print('Valor alto')

jogoAdivinhar()