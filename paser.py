from lexer import lexer
from grammar import parser

# Função para traduzir código JavaScript para Python
def translate_js_to_py(js_code):
    lexer.input(js_code)
    result = parser.parse(js_code)
    return result

# Teste simples
js_code = "var x = 42;"
py_code = translate_js_to_py(js_code)
print(f"Código JavaScript: {js_code}")
print(f"Código Python: {py_code}")
