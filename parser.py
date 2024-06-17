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

def p_program(p):
    'program : declaration_list'
    p[0] = ('program', p[1])

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_declaration(p):
    '''declaration : variable_declaration
                   | function_declaration
                   | type_declaration'''
    p[0] = p[1]

def p_variable_declaration(p):
    '''variable_declaration : type IDENTIFIER EQUALS expression SEMICOLON
                            | VAR IDENTIFIER EQUALS expression SEMICOLON'''
    variables[p[2]] = p[4]
    p[0] = ('var_decl', p[2], p[4])

def p_function_declaration(p):
    'function_declaration : FUNCTION IDENTIFIER params block'
    functions[p[2]] = {'params': p[3], 'block': p[4]}
    p[0] = ('func_decl', p[2], p[3], p[4])
    print(f"Function declaration: {p[2]} with params {p[3]} and block {p[4]}")

def p_params(p):
    '''params : LPAREN param_list RPAREN
              | LPAREN RPAREN'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []
    print(f"Params: {p[0]}")

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_param(p):
    'param : type IDENTIFIER'
    p[0] = (p[1], p[2])

def p_block(p):
    'block : LBRACE statement_list RBRACE'
    p[0] = p[2]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : assignment_statement
                 | condition_statement
                 | loop_statement
                 | return_statement
                 | read_statement
                 | print_statement
                 | function_call_statement
                 | block
                 | SEMICOLON'''
    p[0] = p[1] if p[1] else ('empty',)

def p_assignment_statement(p):
    '''assignment_statement : IDENTIFIER EQUALS expression SEMICOLON'''
    p[0] = ('assign', p[1], p[3])

def p_condition_statement(p):
    '''condition_statement : HAVING LPAREN condition RPAREN DO block END
                           | HAVING LPAREN condition RPAREN DO statement END'''
    p[0] = ('if', p[3], p[6])

def p_loop_statement(p):
    'loop_statement : FOR LPAREN IDENTIFIER IN expression RPAREN DO statement_list END'
    p[0] = ('for', p[3], p[5], p[8])

def p_return_statement(p):
    '''return_statement : RETURN expression SEMICOLON
                        | RETURN SEMICOLON'''
    if len(p) == 4:
        p[0] = ('return', p[2])
    else:
        p[0] = ('return', None)

def p_read_statement(p):
    'read_statement : GET designator SEMICOLON'
    p[0] = ('read', p[2])

def p_print_statement(p):
    '''print_statement : SHOW expression SEMICOLON'''
    print(f"Print statement: show {p[2]}")
    p[0] = ('print', p[2])

def p_function_call_statement(p):
    '''function_call_statement : function_call SEMICOLON'''
    p[0] = p[1]

def p_function_call(p):
    '''function_call : IDENTIFIER LPAREN expression_list RPAREN
                     | IDENTIFIER LPAREN RPAREN'''
    if len(p) == 4:
        p[0] = ('func_call', p[1], [])
    else:
        p[0] = ('func_call', p[1], p[3])

def p_expression_list(p):
    '''expression_list : expression_list COMMA expression
                       | expression'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_condition(p):
    'condition : expression relop expression'
    p[0] = ('condition', p[1], p[2], p[3])

def p_relop(p):
    '''relop : EQ
             | NEQ
             | GT
             | GTE
             | LT
             | LTE'''
    p[0] = p[1]

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = ('add', p[1], p[3])
        elif p[2] == '-':
            p[0] = ('sub', p[1], p[3])
    else:
        p[0] = p[1]

def p_expression_function_call(p):
    '''expression : function_call'''
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
    if len(p) == 2:
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

def p_type_declaration(p):
    'type_declaration : TYPE COLON type'
    p[0] = ('type_decl', p[3])

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