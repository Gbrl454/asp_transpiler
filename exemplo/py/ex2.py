def define_vencedor(jogador1:str, jogador2:str, rodada:int)->None:    
    if jogador1 == 'pedra' and jogador2 == 'tesoura':
        print(f'Jogador 1 venceu a rodada {rodada}')
    elif jogador1 == 'papel' and jogador2 == 'pedra':
        print(f'Jogador 1 venceu a rodada {rodada}')
    elif jogador1 == 'tesoura' and jogador2 == 'papel':
        print(f'Jogador 1 venceu a rodada {rodada}')
    elif jogador1 == 'pedra' and jogador2 == 'papel':
        print(f'Jogador 2 venceu a rodada {rodada}')
    elif jogador1 == 'papel' and jogador2 == 'tesoura':
        print(f'Jogador 2 venceu a rodada {rodada}')
    elif jogador1 == 'tesoura' and jogador2 == 'pedra':
        print(f'Jogador 2 venceu a rodada {rodada}')
    else:
        print('Empate')

print('* Pedra, Papel e Tesoura *')
print('Rodadas: ')
qRodadas = int(input())

for i in range(qRodadas):
    print('Jogador 1: ')
    jogador1 = input()
    print('Jogador 2: ')
    jogador2 = input()

    define_vencedor(jogador1, jogador2, i+1)