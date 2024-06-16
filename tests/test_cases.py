import unittest
from parser import parser
from codegen.py import generate_code

class TestTranspiler(unittest.TestCase):
    def test_simple_assignment(self):
        code = "int main() { int x = 10; }"
        ast = parser.parse(code)
        python_code = generate_code(ast)
        expected = "def main():\n\tint x = 10"
        self.assertEqual(python_code.strip(), expected.strip())

    def test_print_statement(self):
        code = "int main() { print(10, 1); }"
        ast = parser.parse(code)
        python_code = generate_code(ast)
        expected = "def main():\n\tprint(10)"
        self.assertEqual(python_code.strip(), expected.strip())

if __name__ == '__main__':
    unittest.main()
