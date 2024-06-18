import ply.yacc as yacc
from lexer import tokens

# Dicionário para armazenar variáveis e funções
variables = {}
functions = {}

# Precedência dos operadores
precedence = (
    ('left', 'EITHER', 'OR'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD', 'BY'),
    ('right', 'EQUALS'),
)

# Regras da gramática
def p_print_statement(p):
    '''print_statement : SHOW CHARCONST'''
    print(f"Print statement: show {p[2]}")
    p[0] = ('print', p[2])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Constrói o parser
parser = yacc.yacc()
