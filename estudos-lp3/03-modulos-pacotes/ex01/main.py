from funcoes1 import *

comprimento = float(input('Digite o comprimento em centímetros: '))
altura = float(input('Digite a altura em centímetros: '))
largura = float(input('Digite a largura em centímetros: '))

volume = calcVolume(comprimento, altura, largura)

print()
print(f'O volume do aquário em litros é: {volume:.2f}')

tempDesejada = float(input('Digite a temperatura do aquário desejada: '))

while True:
    tempAmbiente = float(input('Digite a temperatura ambiente: '))
    if tempDesejada >= tempAmbiente:
        break
    print('Temperatura ambiente deve ser maior ou igual a temperatura desejada para o uso do termostato')

potencia = calcPotencia(volume, tempDesejada, tempAmbiente)

print()
print(f'A potência necessária do termostato para atingir a temperatura desejada é: {potencia:.1f}')

print()
print(f'A quantidade de filtragem de litros por hora é entre {volume*2:.0f} e {volume*3:.0f}')