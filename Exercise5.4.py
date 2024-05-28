proceed = True
while proceed:
    count = 1
    D = int(input('\nDigite um número maior que Zero: '))
    while D <= 0:
        D = int(input('\nDigite um número maior que Zero: '))
    L = int(input('Digite o limite: '))
    if L <= 0:
        print(f'TAMANHO {L} INVALIDO')
    else:
        while count <= L:
            if count % D == 0:
                print(count, end='  ')
            count += 1
    print('Fim.')
    proceed = 'Erro'
    while proceed == 'Erro':
        proceed = input('\nContinuar? S/N: ')
        if proceed == 'S':
            proceed = True
        elif proceed == 'N':
            print('Fim da Execução.')
            proceed = False
        else:
            print('Digite um valor Válido(S/N)')
            proceed = 'Erro'
