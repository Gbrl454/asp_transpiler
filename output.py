print('Quantidade de alunos: ')
qAlunos: int = int(input())

total_notas: float = 0
total_aprovados: float = 0
menor_nota: float = None
maior_nota: float = None

for i in range(qAlunos):
    print('Nota: ')
    nota: float = float(input())

print('Media: ' + total_notas / qAlunos)
print('Alunos aprovados: ' + total_aprovados)
print('Alunos reprovados: ' + qAlunos - total_aprovados)
print('Menor nota: ' + menor_nota)
print('Maior nota: ' + maior_nota)