print('Quantidade de alunos: ')
qAlunos = int(input())

total_notas = 0
total_aprovados = 0
menor_nota = None
maior_nota = None

for i in range(qAlunos):
    print('Nota: ')
    nota = float(input())
    total_notas += nota

    if menor_nota is None or nota < menor_nota:
        menor_nota = nota

    if maior_nota is None or nota > maior_nota:
        maior_nota = nota

    if nota >= 7:
        print('Aprovado')
        total_aprovados += 1
    else:
        print('Reprovado')

print(f'Media: {total_notas/qAlunos}')
print(f'Alunos aprovados: {total_aprovados}')
print(f'Alunos reprovados: {qAlunos - total_aprovados}')
print(f'Menor nota: {menor_nota}')
print(f'Maior nota: {maior_nota}')