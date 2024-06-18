from l import lexer
from p import parser

data = '''
show 'oi'
'''

lexer.input(data)

print("Tokens:")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# Parsea a entrada
print("\nParsing:")
result = parser.parse(data)

# # Mostra as variáveis e funções
# print("\nVariables:")
# for var, value in variables.items():
#     print(f"{var} = {value}")
#
# print("\nFunctions:")
# for func, details in functions.items():
#     print(f"{func} = {details}")