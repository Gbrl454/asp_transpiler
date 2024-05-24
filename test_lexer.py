from lexer import lexer

def test_lexer(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Testes simples
data = "having cpfVAlido by cpf.length = 11"

test_lexer(data)
