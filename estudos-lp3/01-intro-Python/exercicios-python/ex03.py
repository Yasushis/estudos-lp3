valor = float(input('Digite o valor da sua compra: '))

if valor < 10:
    print(f'Desconto aplicado -> 0')
    print(f'Valor final com desconto -> {valor}')
    
elif valor < 100:
    print(f'Desconto aplicado -> {valor * 0.05:.2f}')
    print(f'Valor final com desconto -> {valor - valor * 0.05:.2f}')

elif valor < 500:
    print(f'Desconto aplicado -> {valor * 0.1:.2f}')
    print(f'Valor final com desconto -> {valor - valor * 0.1:.2f}')

else:
    print(f'Desconto aplicado -> {valor * 0.15:.2f}')
    print(f'Valor final com desconto -> {valor - valor * 0.15:.2f}')
