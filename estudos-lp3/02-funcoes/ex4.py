def eleicao():

    candidato1 = 'Pedro'
    candidato2 = 'Ugo'
    candidato3 = 'Fátima'

    voto1 = 0
    voto2 = 0
    voto3 = 0

    while True:

        voto = input(f'Vote em um candidato: \n1:{candidato1} \n2:{candidato2} \n3:{candidato3} \n0:Encerrar programa\n')

        if voto == '1':
            voto1 += 1
        elif voto == '2':
            voto2 += 1
        elif voto == '3':
            voto3 += 1
        elif voto == '0':
            break
        else:
            print('Voto inválido, vote novamente')
        print()
    print('---------RESULTADO---------')
    print(f'{candidato1}:{voto1}\n{candidato2}:{voto2}\n{candidato3}:{voto3}')
    
    if voto1 > voto2 and voto1 > voto3:
        print(f'{candidato1} é o(a) vencedor(a)!')
    elif voto2 > voto3 and voto2 > voto1:
        print(f'{candidato2} é o(a) vencedor(a)!')
    elif voto3 > voto2 and voto3 > voto1:
        print(f'{candidato3} é o(a) vencedor(a)!')
    else:
        print('Empate!')
eleicao()