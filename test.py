from lexer import lexer
from parser import parser

data = '''
int x = 5;
int y = 10;
int z = x + y;
function add(int a, int b) {
    return a + b;
}
y = add(x, z);
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

# Mostra as variáveis e funções
print("\nVariables:")
for var, value in variables.items():
    print(f"{var} = {value}")

print("\nFunctions:")
for func, details in functions.items():
    print(f"{func} = {details}")