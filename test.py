from lexer import lexer
from parser import parser

data = '''
show 'Alunos aprovados: ' + 0;
'''

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
print("\nParsing:")
result = parser.parse(data)


def loop(l):
    code = ''
    for i in l:
        if type(i) == tuple:
            code += loop(i)
        else:
            code += str(i)
    return code


print("\n")
print(loop(result))
