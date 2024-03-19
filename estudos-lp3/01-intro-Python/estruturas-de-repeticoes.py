# for, while, break, continue

# operador in

palavra = 'Pyhton'

for letra in 'Python':
    print(letra)

itens = ['banana', 'arroz', 'limão']

for item in itens:
    print(item)

for i in range(5):
    print(i)


lista = []

list = list(range(101))

print(type(lista))

# while

contador = 0

while contador <= 5:
    print(contador)
    contador += 1


# break
numeros = list(range(10))

for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break

# continue

for numero in numeros:
    if numero <= 0:
        continue
    print(numero)


numerolos = [2, 3, 4, 5, 6]

for numero in numerolos:
    numerolos.replace(numero, numero**2)

palavra = 'Ola Mundo!'
letras = []
for letra in palavra:
    letras.append(letra)

letras = [letra for letra in palavra]