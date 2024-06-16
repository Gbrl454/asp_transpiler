import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''program : FunctionDeclaration
               | FunctionDeclaration program'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[2]

def p_FunctionDeclaration(p):
    'FunctionDeclaration : Type IDENT Params Block'
    p[0] = ('function', p[1], p[2], p[3], p[4])

def p_Params(p):
    '''Params : LPAREN RPAREN
              | LPAREN param_list RPAREN'''
    p[0] = p[2] if len(p) == 4 else []

def p_param_list(p):
    '''param_list : param
                  | param COMMA param_list'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[3]

def p_param(p):
    'param : Type IDENT'
    p[0] = (p[1], p[2])

def p_Block(p):
    'Block : LBRACE statement_list RBRACE'
    p[0] = ('block', p[2])

def p_statement_list(p):
    '''statement_list : Statement
                      | Statement statement_list'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[2]

def p_Statement(p):
    '''Statement : Designator EQUAL Expr SEMI
                 | Designator ActPars SEMI
                 | HAVING Condition THEN Statement ELSE Statement
                 | AS Condition DO Statement
                 | RETURN Expr SEMI
                 | READ Designator SEMI
                 | PRINT Expr COMMA NUMBER SEMI
                 | Block
                 | SEMI'''
    if len(p) == 5 and p[2] == '=':
        p[0] = ('assign', p[1], p[3])
    elif len(p) == 4:
        p[0] = ('call', p[1], p[2])
    elif len(p) == 7:
        p[0] = ('if', p[2], p[4], p[6])
    elif len(p) == 5:
        p[0] = ('while', p[2], p[4])
    elif len(p) == 3 and p[1] == 'return':
        p[0] = ('return', p[2])
    elif len(p) == 3 and p[1] == 'read':
        p[0] = ('read', p[2])
    elif len(p) == 5 and p[1] == 'print':
        p[0] = ('print', p[2], p[4])
    elif len(p) == 3 and p[1] == ';':
        p[0] = ('empty',)
    else:
        p[0] = p[1]  # Block

def p_ActPars(p):
    '''ActPars : Expr
               | Expr COMMA ActPars'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_Condition(p):
    'Condition : Expr Relop Expr'
    p[0] = ('condition', p[1], p[2], p[3])

def p_Relop(p):
    '''Relop : EQ
             | NEQ
             | GT
             | GTE
             | LT
             | LTE'''
    p[0] = p[1]

def p_Expr(p):
    '''Expr : Term
            | Expr Addop Term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_Term(p):
    '''Term : Factor
            | Term Mullop Factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_Factor(p):
    '''Factor : Designator
              | NUMBER
              | CHARCONST
              | NEW IDENT
              | LPAREN Expr RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]
    elif p[1] == 'new':
        p[0] = ('new', p[2])

def p_Designator(p):
    '''Designator : IDENT
                  | IDENT DOT IDENT
                  | IDENT LPAREN ActPars RPAREN'''
    if len(p) == 2:
        p[0] = ('ident', p[1])
    elif len(p) == 4:
        p[0] = ('access', p[1], p[3])
    elif len(p) == 5:
        p[0] = ('call', p[1], p[3])

def p_Addop(p):
    '''Addop : PLUS
             | MINUS'''
    p[0] = p[1]

def p_Mullop(p):
    '''Mullop : TIMES
              | DIVIDE
              | MOD'''
    p[0] = p[1]

def p_Type(p):
    '''Type : INT
            | BOOLEAN
            | TEXT
            | NUMBER_TYPE
            | IDENT'''
    p[0] = p[1]

def p_error(p):
    print(f"Erro de sintaxe em '{p.value}'")

parser = yacc.yacc()
