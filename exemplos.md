# Instuções de entrada e saída

- PYTHON:
  nome = input("Digite seu nome: ")
  print("Olá ", nome)

- Linguagem propria
  get txt:nome by "Digite seu nome: ";
  show "Olá " nome;

# logiacas de laços

- PYTHON:

contador = 0
while contador < 5:
print(f"Contagem: {contador}")
contador += 1

for i in range(1, 6):
print(f"Valor: {i}")

- Linguagem propria:
  int:contador = 0;
  while contador < 5 do
  show "Contagem: " contador;
  contador += 1;
  end

for i in range(1 to 6) do
show "Contagem" contador;
end

# Estruturas de controle

- PYTHON:
  if values.vigencia && values.corrente:
  ativa = true
  else:
  ativa = false

- Linguagem propria:
  having values.vigencia AND values.corrente not do
  ativa = true
  either
  ativa = false
  end

# Declaração de funções/metodos

- PYTHON:
  def cpfValido(cpf, nome):
  return cpf.lenght == 11

print(cpfValido(cpf, nome))

- Linguagem propria
  handler bool:cpfValido with txt:cpf and txt:nome doing
  return cpf.lenght == 11
  end

show cpfValido(values.cpf, values.nome)

# Explessoões aritméticas e booleansas

- PYTHON:
  x = 5
  y = 3
  maior = x > y
  igual = x == y
  print(f"x é maior que y? {maior}, x é igual a y? {igual}")

- Linguagem propria
  int:x = 5
  int:y = 3
  bool:maior = x > y
  bool:igual = x == y
  show "x é maior que y?" maior "x é igual a y?" igual;
