proceed = True
while proceed:
    N = int(input('\nDigite um Número: '))
    S = int(input('Digite o tamanho da Tabuada: '))
    count = 0

    if S > 0:
        while count <= S:
            print(f'{N} x {count} = {N * count}')
            count += 1
    elif S < 0:
        while count >= S:
            print(f'{N} x {count} = {N * count}')
            count -= 1
    else:
        print(f'TAMANHO {S} INVALIDO')
    while proceed:
        proceed = input('\nContinuar? S/N: ')
        if proceed == 'N' or proceed == 'n':
            print('Fim da Execução')
            proceed = False
        elif proceed != 'S' or proceed != 's':
            print('Digite um valor Válido(S/N): ')
            continue
        else:
            continue
