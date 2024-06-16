from lexer import lexer
from parser import parser
# Script de exemplo
data = """
get int:qAlunos by 'Quantidade de alunos: ';

float:total_notas = 0;
float:total_aprovados = 0;
float:menor_nota = null;
float:maior_nota = null;

for i in range qAlunos do
    get float:nota by 'Nota: ';
    total_notas += nota;

    having menor_nota == null or nota < menor_nota do
        menor_nota = nota;
    end

    having maior_nota == null or nota > maior_nota do
        maior_nota = nota;
    end

    having nota >= 7 do
        show 'Aprovado';
        total_aprovados += 1;
    either
        show 'Reprovado';
    end

show 'Media: ' (total_notas/qAlunos);
show 'Alunos aprovados: ' total_aprovados;
show 'Alunos reprovados: ' (qAlunos - total_aprovados);
show 'Menor nota: ' menor_nota;
show 'Maior nota: ' maior_nota;
"""

# Tokeniza e analisa o código de exemplo
# lexer.input(data)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

# # Analisa o código de exemplo
result = parser.parse(data)
# print("Parsing completed!")
# print("Variables:", variables)
# print("Functions:", functions)
