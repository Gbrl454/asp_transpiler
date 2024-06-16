# asp_tec_transpilador
ASPECTOS TEÓRICOS COMPUTAÇÃO - AV3

## Descrição
Este projeto é um transpilador que converte uma linguagem própria para Python. A linguagem de origem suporta declarações de variáveis, funções, condições, loops, e expressões aritméticas.

## Estrutura do Projeto
- `lexer.py`: Implementação do analisador léxico.
- `parser.py`: Implementação do analisador sintático.
- `codegen.py`: Implementação da análise semântica e geração de código.
- `tests/test_cases.py`: Casos de teste para validar o transpilador.

## Como Executar
1. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   pip install ply

