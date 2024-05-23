from lexer import lexer


def test_lexer(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Testes simples
data = '''cpfValido HAVING cpf.length = 11 DO true;'''

test_lexer(data)
