from lexer import lexer
from parser import parser, variables, functions

data = """get int:qAlunos by 'Quantidade de alunos: ';

float:total_notas = 0;
float:total_aprovados = 0;
float:menor_nota = null;
float:maior_nota = null;

show 'Maior nota: ' + maior_nota;
"""

# Alimenta o lexer com dados de entrada
lexer.input(data)

# Tokeniza a entrada
print("Tokens:")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# Parsea a entrada
result = parser.parse(data)

print("\nParsing completed!")
print("Variables:", variables)
print("Functions:", functions)


code = ""

def loop(l):
    code = ""
    if l != None:
        for i in l:
            if type(i) == tuple:
                code += loop(i)
            else:
                code += str(i)
    return code

code += loop(result)
with open("output.py", 'w') as file:
    file.write(code)