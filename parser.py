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
    '''print_statement : SHOW expression SEMICOLON'''
    print(f"Print statement: show {p[2]} {p[3]}")
    p[0] = ('print','(', p[2],')')

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = (p[1],' + ', p[3])
        elif p[2] == '-':
            p[0] = ( p[1],' - ', p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | term MOD factor
            | factor'''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = ('mul', p[1], p[3])
        elif p[2] == '/':
            p[0] = ('div', p[1], p[3])
        elif p[2] == '%':
            p[0] = ('mod', p[1], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | FLOAT
              | CHARCONST
              | LPAREN expression RPAREN
              | designator'''
    if len(p) == 2 and type(p[1]) == str:
        p[0] = "'" + p[1] + "'"
    elif len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]
    print(f"Factor: {p[0]}")

def p_designator(p):
    '''designator : IDENTIFIER
                  | designator DOT IDENTIFIER'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = f"{p[1]}.{p[3]}"

def p_type(p):
    '''type : INT
            | BOOLEAN
            | TEXT
            | FLOAT
            | IDENTIFIER'''
    p[0] = p[1]
    print(f"Type: {p[0]}")

def p_null(p):
    'expression : NULL'
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Constrói o parser
parser = yacc.yacc()

# teste
if __name__ == "__main__":
    data = '''
    function add(a, b) {
        return a + b;
    }
    '''
    result = parser.parse(data)
    print(result)# type: ignore