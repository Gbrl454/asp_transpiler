from parser import parser

def generate_code(node):
    if isinstance(node, tuple):
        if node[0] == 'function':
            _, return_type, name, params, body = node
            param_str = ', '.join(p[1] for p in params)
            body_code = generate_code(body)
            return f"def {name}({param_str}):\n{body_code}"
        elif node[0] == 'block':
            statements = '\n'.join(generate_code(stmt) for stmt in node[1])
            return f"{statements}"
        elif node[0] == 'assign':
            return f"{node[1][1]} = {generate_code(node[2])}"
        elif node[0] == 'call':
            return f"{node[1][1]}({', '.join(generate_code(arg) for arg in node[2])})"
        elif node[0] == 'if':
            cond = generate_code(node[1])
            then = generate_code(node[2])
            else_ = generate_code(node[3])
            return f"if {cond}:\n\t{then}\nelse:\n\t{else_}"
        elif node[0] == 'while':
            cond = generate_code(node[1])
            body = generate_code(node[2])
            return f"while {cond}:\n\t{body}"
        elif node[0] == 'return':
            return f"return {generate_code(node[1])}"
        elif node[0] == 'read':
            return f"{node[1][1]} = input()"
        elif node[0] == 'print':
            return f"print({generate_code(node[1])})"
        elif node[0] == '+':
            return f"({generate_code(node[1])} + {generate_code(node[2])})"
        elif node[0] == '-':
            return f"({generate_code(node[1])} - {generate_code(node[2])})"
        elif node[0] == '*':
            return f"({generate_code(node[1])} * {generate_code(node[2])})"
        elif node[0] == '/':
            return f"({generate_code(node[1])} / {generate_code(node[2])})"
        elif node[0] == '%':
            return f"({generate_code(node[1])} % {generate_code(node[2])})"
        elif node[0] == 'new':
            return f"{node[1]}()"
    elif isinstance(node, list):
        return '\n'.join(generate_code(n) for n in node)
    else:
        return str(node)

# Exemplo de uso
code = """
int main() {
    int x = 10;
    print(x, 1);
}
"""
ast = parser.parse(code)
python_code = generate_code(ast)
print(python_code)
