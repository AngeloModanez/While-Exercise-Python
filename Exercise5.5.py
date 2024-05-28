proceed = True
while proceed:
    total = qty = 0
    print("\nDigite um valor para somar, e para encerrar digite '0'")
    A = int(input('Digite um Valor: '))
    while A != 0:
        total = total + A
        qty += 1
        A = int(input('Digite um Valor: '))
    print(f'\nSoma dos Valores = {total}')
    print(f'Quantidade = {qty}')
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
