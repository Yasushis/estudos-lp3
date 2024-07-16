from funcoes2 import *

kg = float(input('Digite o seu peso em quilogramas: '))
altura = float(input('Digite a sua altura em metros: '))

imc = calcIMC(altura, kg)

ideal = pesoIdeal(altura)

if imc < 18.5:

    print('Classificação: Baixo Peso')
    print(f'Com base em sua altura, seu peso ideal seria: {ideal:.2f}. Você precisa ganhar {ideal-kg:.2f} quilos.')

elif imc < 25:

    print('Classificação: Peso Normal')

elif imc < 30:

    print('Classificação: Excesso de peso')
    print(f'Com base em sua altura, seu peso ideal seria: {ideal:.2f}. Você precisa perder {kg-ideal:.2f} quilos.')

elif imc < 35:

    print('Classificação: Obesidade de Classe 1')
    print(f'Com base em sua altura, seu peso ideal seria: {ideal:.2f}. Você precisa perder {kg-ideal:.2f} quilos.')

elif imc < 40:

    print('Classificação: Obesidade de Classe 2')
    print(f'Com base em sua altura, seu peso ideal seria: {ideal:.2f}. Você precisa perder {kg-ideal:.2f} quilos.')

else:

    print('Classificação: Obesidade de Classe 3')
    print(f'Com base em sua altura, seu peso ideal seria: {ideal:.2f}. Você precisa perder {kg-ideal:.2f} quilos.')