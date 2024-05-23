import ply.lex as lex

# Lista de tokens
tokens = (
    'IDENT',
    'TRUE',
    'FALSE',
    'TEXT',
    'STRING',
    'NUMBER',
    'CHARCONST',
    'EQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMI',
    'COMMA',
    'DOT',
    'EQ',
    'NEQ',
    'GT',
    'GTE',
    'LT',
    'LTE',
)

# Expressões regulares para tokens simples
t_EQUAL = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','
t_DOT = r'\.'
t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_GTE = r'>='
t_LT = r'<'
t_LTE = r'<='
t_TRUE = r'true'
t_FALSE = r'false'
t_TEXT = r'text'

# Regras de expressões regulares com ações
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = t.value.strip('"') 
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignora espaços e tabs
t_ignore = ' \t'

# Regra para rastrear números de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra de erro
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construindo o lexer
lexer = lex.lex()
