import ply.yacc as yacc
from lexer import tokens

tokens = tokens

# Dicionário para armazenar variáveis e funções
variables = {}
functions = {}

# Precedência dos operadores
precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE", "MOD"),
    ("right", "EQUALS"),
)

# Regras da gramática
def p_program(p):
    "program : declaration_list"
    p[0] = p[1]

def p_newline_statement(p):
    """newline_statement : NEWLINE
    | newline_statement NEWLINE"""
    if len(p) == 3:
        p[0] = ('\n' ,p[2])
    else:
        p[0] = '\n'


def p_declaration_list(p):
    """declaration_list : declaration_list declaration
                        | declaration"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_declaration(p):
    """declaration : variable_declaration
                   | statement"""
    p[0] = p[1]

def p_variable_declaration(p):
    "variable_declaration : type COLON IDENTIFIER EQUALS expression SEMICOLON"
    variables[p[3]] = (p[5], p[1])
    p[0] = (p[3],': ',p[1],' = ', p[5])

def p_statement(p):
    """statement : read_statement
                 | print_statement
                 | for_statement
                 | newline_statement"""
    p[0] = p[1]

def p_print_statement(p):
    """print_statement : SHOW expression SEMICOLON"""
    p[0] = ("print","(", p[2],")")

def p_read_statement(p):
    """read_statement : GET type COLON IDENTIFIER BY expression SEMICOLON"""
    variables[p[4]] = (p[6], p[1])
    p[0] = ("print",'(',p[6],')','\n',p[4],': ' + p[2],' = ', p[2],'(','input()',')')

def loop(l):
    code = []
    if l != None:
        for i in l:
            code.append(loop(i) if type(i) in (tuple, list) else i.replace('\n','\n    '))
    if '\n' in code[-1]:
        code [-1] =''
    return code

def p_for_statement(p):
    """for_statement : FOR IDENTIFIER IN RANGE expression DO NEWLINE declaration_list END"""       
    p[0] = ('for',' ',p[2],' ', 'in', ' ', 'range', '(',p[5],')',':','\n    ',loop(p[8]))

def p_expression(p):
    """expression : expression PLUS term
                  | expression MINUS term
                  | term"""
    if len(p) == 4:
        if p[2] == '+':
            p[0] = (p[1], ' + ', p[3])
        elif p[2] == '-':
            p[0] = (p[1] ,' - ', p[3])
    else:
        p[0] = p[1]

def p_term(p):
    """term : term TIMES factor
            | term DIVIDE factor
            | term MOD factor
            | factor"""
    if len(p) == 4:
        if p[2] in ('+','-','*','/','%'):
            p[0] = (p[1]," ",p[2]," ",p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | FLOAT
              | CHARCONST
              | LPAREN expression RPAREN
              | designator'''
    if len(p) == 2 and type(p[1]) == str and p[1] not in variables.keys():
        p[0] = "'" + p[1] + "'"
    elif len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]

def p_designator(p):
    """designator : IDENTIFIER
                  | designator DOT IDENTIFIER"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + '.' + p[3]

def p_type(p):
    """type : INT
            | BOOLEAN
            | TEXT
            | FLOAT"""
    p[0] = p[1]

def p_null(p):
    "expression : NULL"
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
 # type: ignore