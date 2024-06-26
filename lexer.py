import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'IDENTIFIER',
    'CHARCONST',
    'INT',
    'BOOLEAN',
    'TEXT',
    'FUNCTION',
    'GET',
    'BY',
    'FLOAT',
    'NULL',
    'FOR',
    'IN',
    'DO',
    'HAVING',
    'OR',
    'END',
    'EITHER',
    'SHOW',
    'RETURN',
    'EQUALS',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'DOT',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'EQ',
    'NEQ',
    'GT',
    'GTE',
    'LT',
    'LTE',
    'TYPE'
)

# Regras de expressões regulares para tokens simples
t_EQUALS = r'='
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_GTE = r'>='
t_LT = r'<'
t_LTE = r'<='

# Palavras reservadas
reserved = {
    'int': 'INT',
    'boolean': 'BOOLEAN',
    'text': 'TEXT',
    'float': 'FLOAT',
    'function': 'FUNCTION',
    'get': 'GET',
    'by': 'BY',
    'null': 'NULL',
    'for': 'FOR',
    'in': 'IN',
    'do': 'DO',
    'having': 'HAVING',
    'or': 'OR',
    'end': 'END',
    'either': 'EITHER',
    'show': 'SHOW',
    'return': 'RETURN',
}

# Regras de expressões regulares com ações
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_INT(t):
    r'\bint\b'
    return t

def t_BOOLEAN(t):
    r'\bboolean\b'
    return t

def t_FLOAT(t):
    r'\bfloat\b'
    return t

def t_NULL(t):
    r'\bnull\b'
    return t

def t_FOR(t):
    r'\bfor\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_DO(t):
    r'\bdo\b'
    return t

def t_HAVING(t):
    r'\bhaving\b'
    return t

def t_OR(t):
    r'\bor\b'
    return t

def t_END(t):
    r'\bend\b'
    return t

def t_EITHER(t):
    r'\beither\b'
    return t

def t_SHOW(t):
    r'\bshow\b'
    return t

def t_RETURN(t):
    r'\breturn\b'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHARCONST(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value.strip("'")
    return t

# Ignora espaços e tabs
t_ignore = ' \t'

# Ignora comentários
def t_comment(t):
    r'//.*'
    pass

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