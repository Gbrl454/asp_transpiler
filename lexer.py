import ply.lex as lex

# Lista de tokens
tokens = (
    'IDENT', 'NUMBER', 'CHARCONST',
    'EQUAL', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA', 'DOT',
    'EQ', 'NEQ', 'GT', 'GTE', 'LT', 'LTE',
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

# Palavras-chave
reserved = {
    'new': 'NEW',
    'return': 'RETURN',
    'read': 'READ',
    'print': 'PRINT',
    'having': 'HAVING',
    'then': 'THEN',
    'else': 'ELSE',
    'as': 'AS',
    'do': 'DO',
    'int': 'INT',
    'boolean': 'BOOLEAN',
    'text': 'TEXT',
    'number': 'NUMBER_TYPE'
}

# Adiciona as palavras reservadas aos tokens
tokens += tuple(reserved.values())

# Regras para tokens complexos
def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHARCONST(t):
    r'\'([^\\\n]|(\\.))*?\''
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Contagem de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Erros de caracteres ilegais
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
