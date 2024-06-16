import ply.yacc as yacc
from lexer import tokens

tokens = tokens

# Dicionário para armazenar variáveis e funções
variables = {}
functions = {}

# Precedência dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'UMINUS'),
)

# Regras da gramática

def p_program(p):
    'program : declaration_list'
    pass

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    pass

def p_declaration(p):
    '''declaration : variable_declaration
                   | function_declaration'''
    pass

def p_variable_declaration(p):
    'variable_declaration : TYPE IDENTIFIER EQ expression SEMI'
    variables[p[2]] = p[4]

def p_function_declaration(p):
    'function_declaration : TYPE IDENTIFIER params block'
    functions[p[2]] = {'params': p[3], 'block': p[4]}

def p_params(p):
    '''params : LPAREN param_list RPAREN
              | LPAREN RPAREN'''
    p[0] = p[2] if len(p) == 4 else []

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_param(p):
    'param : TYPE IDENTIFIER'
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
                 | block
                 | SEMI'''
    pass

def p_assignment_statement(p):
    '''assignment_statement : designator EQ expression SEMI
                            | designator ActPars SEMI'''
    pass

def p_condition_statement(p):
    '''condition_statement : HAVING condition THEN statement ELSE statement
                           | HAVING condition THEN statement'''
    pass

def p_loop_statement(p):
    'loop_statement : AS condition DO statement'
    pass

def p_return_statement(p):
    '''return_statement : RETURN expression SEMI
                        | RETURN SEMI'''
    pass

def p_read_statement(p):
    'read_statement : READ designator SEMI'
    pass

def p_print_statement(p):
    '''print_statement : PRINT expression COMMA NUMBER SEMI
                       | PRINT expression SEMI'''
    pass

def p_actpars(p):
    '''ActPars : LPAREN expression_list RPAREN
               | LPAREN RPAREN'''
    p[0] = p[2] if len(p) == 4 else []

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
    pass

def p_relop(p):
    '''relop : EQ
             | RELOP'''
    pass

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | term MOD factor
            | factor'''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        elif p[2] == '%':
            p[0] = p[1] % p[3]
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : designator ActPars
              | NUMBER
              | CHARCONST
              | NEW IDENTIFIER LPAREN expression RPAREN
              | LPAREN expression RPAREN
              | designator'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4 and p[1] == '(':
        p[0] = p[2]
    elif len(p) == 5 and p[1] == 'new':
        p[0] = f"new {p[2]}({p[4]})"
    else:
        p[0] = p[1]

def p_designator(p):
    '''designator : IDENTIFIER
                  | designator DOT IDENTIFIER
                  | designator LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = f"{p[1]}.{p[3]}"
    else:
        p[0] = f"{p[1]}({p[3]})"

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Constrói o parser
parser = yacc.yacc() # type: ignore