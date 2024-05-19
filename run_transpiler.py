from parser import parser
from codegen import generate_code

# Função para ler o arquivo de entrada
def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Função principal para rodar o transpilador
def main():
    input_code = read_input_file('input_code.txt')
    ast = parser.parse(input_code)
    python_code = generate_code(ast)
    print("Código Python gerado:\n")
    print(python_code)

    # Opcional: Salvar o código Python gerado em um arquivo
    with open('output_code.py', 'w') as file:
        file.write(python_code)

if __name__ == '__main__':
    main()
