def home():
    print('\n-----------------------\n')
    print('Bem vindo')
    print('1 - Ir para exemplo 1')
    print('2 - Ir para exemplo 2')
    print('3 - Sair')

while True:
    home()
    print('Selecione uma opção: ')
    op = int(input())
    if op == 1:
        import ex1
    elif op == 2:
        import ex2
    elif op == 3:
        break
    else:
        print('Opção inválida')