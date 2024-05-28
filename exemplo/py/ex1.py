print('Quantidade de alunos: ')
qAlunos = int(input())

for i in range(qAlunos):
    print('Nota: ')
    nota = float(input())
    if nota >= 7:
        print('Aprovado')
    else:
        print('Reprovado')