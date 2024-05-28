proceed = True
while proceed:
    P = int(input('\nDigite o primeiro Termo: '))
    R = int(input('Digite a Razão: '))
    S = int(input('Digite o Tamanho da PA: '))
    count = 1

    while S <= 0:
        S = int(input(f'\nTamanho {S} invalido: '))

    while count <= S:
        print(P, end=', ')
        P = P + R
        count += 1
    print('Fim da PA.')
    proceed = 'Erro'
    while proceed == 'Erro':
        proceed = input('\nContinuar? S/N: ')
        if proceed == 'S':
            proceed = True
        elif proceed == 'N':
            print('Fim da Execução.')
            proceed = False
        else:
            print('Digite um valor Válido(S/N): ')
            proceed = 'Erro'
