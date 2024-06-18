from lexer import lexer
from parser import parser, variables, functions

data = ""
with open('input.cap', 'r') as file:
    data = file.read()

# Alimenta o lexer com dados de entrada
lexer.input(data)

# Tokeniza a entrada
# print("Tokens:")
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

# Parsea a entrada
result = parser.parse(data)

# print("\nParsing completed!")
# print("Variables:", variables)
# print("Functions:", functions)


code = ""

def loop(l):
    code = ""
    if l != None:
        for i in l:
            code +=  loop(i) if (type(i) in (tuple, list)) else str(i)
    return code

code += loop(result)
with open("output.py", 'w') as file:
    file.write(code)