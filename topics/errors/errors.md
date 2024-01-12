# Erros em python

Em python temos os erros de sintaxe e as exeções. quando um código possui sua sintaxe bem definida, porém acontece algum erro, nos denominamos de erro de exeção. o python possui vários erros de exeções já pré definidos, porém é possível criarmos novas exeções.

## raise + Exception():

Para criarmos uma exeção devemos usar a palavra chave `raise`, juntamente com o método `Exception()`. vamos ver isso em um exemplo:

```python
def calcular_imc(peso, altura):
  if altura <= 0:
    raise Exception(f'a altura de {altura}m é invalida')
    
  return (math.pow(altura,2))/peso
```

neste exemplo, caso o usuário informe uma altura negativa, o código irá lançar uma exeção.

## Assert

Parecido com o anterior, o assert verifica se a condição é verdadeira, caso for, ele continuará o fluxo normal do código, caso contrário, lançará um **AssertionError**.

um exemplo básico temos:

```python
user_log = {}
assert user_log, "o usuario não está logado!"

print("testando...")
for i in range(10):
  for j in range(10):
    if i % 2 == 0:
      print("*")
    else:
      print("-")
```

Em resumo, raise é geralmente utilizado para levantar exceções em condições específicas, enquanto assert é mais voltado para verificar suposições durante o desenvolvimento e depuração.

## try + except