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
    'TYPE',
    'VAR',
    'NEWLINE',
    'RANGE'
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
t_NEWLINE = r'\n'

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
    'var': 'VAR',
    'range': 'RANGE'
}

# Regras de expressões regulares com ações
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
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
    r'\n'
    t.lexer.lineno += len(t.value)
    t.type = 'NEWLINE'
    return t

# Regra de erro
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construindo o lexer
lexer = lex.lex()