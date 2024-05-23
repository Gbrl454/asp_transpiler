from lexer import tokens
import ply.yacc as yacc

# Lista de tokens (necessária pelo yacc)
tokens = tokens

# Definindo a gramática
def p_statement_assign(p):
    'statement : VAR IDENTIFIER EQUALS NUMBER SEMICOLON'
    p[0] = f"{p[2]} = {p[4]}"

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final da entrada")


# Construindo o parser
parser = yacc.yacc()
