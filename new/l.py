import ply.lex as lex

# Lista de tokens
tokens = ('NUMBER',
          'IDENTIFIER',
          'CHARCONST',
          'INT',
          'SHOW')

reserved = {
    'int': 'INT',
    'show': 'SHOW',
}

# Regras de expressões regulares com ações
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
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