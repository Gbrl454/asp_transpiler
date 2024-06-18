import ply.yacc as yacc
from lexer import tokens

typs = ['number', 'float', 'int', 'boolean', 'charconst', 'text', 'null']
tokens = tokens
TAB = '    '

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
    """variable_declaration : factor COLON IDENTIFIER EQUALS expression SEMICOLON
                            | IDENTIFIER EQUALS expression SEMICOLON"""
    if len(p) == 7:
        variables[p[3]] = (p[5], p[1])
        p[0] = (p[3],': ',p[1],' = ', p[5])
    elif len(p) == 3:
        print(variables[p[1]])
        p[0] = (p[1],' = ', p[3])

def p_statement(p):
    """statement : read_statement
                 | print_statement
                 | if_statement
                 | for_statement
                 | newline_statement"""
    p[0] = p[1]

def p_print_statement(p):
    """print_statement : SHOW expression SEMICOLON"""
    p[0] = ("print","(", p[2],")")

def p_read_statement(p):
    """read_statement : GET factor COLON IDENTIFIER BY expression SEMICOLON"""
    variables[p[4]] = (p[6], p[1])
    p[0] = ("print",'(',p[6],')','\n',p[4],': ' + p[2],' = ', p[2],'(','input()',')')

def put_tabs(l):
    code = []
    if l is not None:
        for i in l:
            if i is not None and type(i) != int:
                code.append(put_tabs(i) if isinstance(i, (tuple, list)) else i.replace('\n', '\n'+TAB))
    if code and '\n' in code[-1]:
        code[-1] = ''
    return code


def p_if_statement(p):
    '''if_statement : HAVING condition DO declaration_list END
                    | HAVING condition DO declaration_list EITHER declaration_list END
                    | HAVING condition DO declaration_list EITHER condition DO declaration_list END'''
    if len(p) == 10:
        p[0] = ('if',' ',p[2],':',('\n'+TAB),put_tabs(p[4]),'\nelif',p[6],':',put_tabs(p[8]))
    elif len(p) == 8:
        p[0] = ('if',' ',p[2],':',put_tabs(p[4]),'\nelse:',put_tabs(p[6]))
    else:
        p[0] = ('if',' ',p[2],':',('\n'+TAB),put_tabs(p[4]))

def p_condition(p):
    '''condition : expression'''
    p[0] = p[1]

def p_for_statement(p):
    """for_statement : FOR IDENTIFIER IN RANGE expression DO NEWLINE declaration_list END"""       
    p[0] = ('for',' ',p[2],' ', 'in', ' ', 'range', '(',p[5],')',':',('\n'+TAB),put_tabs(p[8]))

def p_expression(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression EQ expression
                  | expression NEQ expression
                  | expression GT expression
                  | expression GTE expression
                  | expression LT expression
                  | expression LTE expression
                  | expression EQUALS expression
                  | expression OR expression
                  | factor"""
    if len(p) == 4:
        if p[2] in ('+','-','*','/','%','==','!=','>','<','>=','<=','=','or'):
            p[0] = (p[1],' ',p[2],' ',p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | FLOAT
              | INT
              | BOOLEAN
              | CHARCONST
              | TEXT
              | NULL
              | LPAREN expression RPAREN
              | designator'''
    if len(p) == 2:
        if type(p[1]) == str:
            if p[1] == 'null':
                p[0] = 'None'
            elif (p[1] not in variables.keys()) and p[1] not in typs:
                p[0] = "'" + p[1] + "'"
            else:
                p[0] = p[1]
        else:
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

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
 # type: ignore