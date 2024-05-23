import ply.lex as lex

# Lista de tokens
tokens = (
    'VAR',
    'IDENTIFIER',
    'EQUALS',
    'NUMBER',
    'SEMICOLON'
)

# Regras de expressões regulares para tokens simples
t_VAR = r'var'
t_EQUALS = r'='
t_SEMICOLON = r';'

# Regras de expressões regulares com ações
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
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
