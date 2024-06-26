from lexer import lexer

def test_lexer(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Testes simples
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

test_lexer(data)
