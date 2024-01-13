# Erros em python

Em python temos os erros de sintaxe e as exeções. quando um código possui sua sintaxe bem definida, porém acontece algum erro, nos denominamos de erro de exeção. o python possui vários erros de exeções já pré definidos, porém é possível criarmos novas exeções.

## raise + Exception():

Para lançarmos uma exeção devemos usar a palavra chave `raise`, juntamente com o método `Exception()`. vamos ver isso em um exemplo:

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

essas duas palavras reservadas funcionam da seguinte maneira:

```python
try:
  #irá realizar algo no seu codigo até uma exeção for encontrada, caso for enontrada interromperá o código instantaneamente e irá para o except
except:
  #caso houver uma exeção no código acima ele executará essa parte do código, caso contrário, o código seguirá o fluxo normal
```

## else

quando não é encontrado nenhuma exeção no código podemos usar o `else` para tratar algo que não foi "parado" pelo try e except.

```python
try:
  #irá realizar algo no seu codigo até uma exeção for encontrada
except:
  #caso houver uma exeção no codigo acima ele executará essa parte do codigo, caso contrario, o codigo seguirá o fluxo normal
else:
  #executa algo apos verificar o try e except
```

## finally

essa palavra reservada é usada depois do `else` e ela sempre será executada, tendo exeções ou não. O uso típico do bloco `finally` é para garantir que determinadas operações, como fechar arquivos ou liberar recursos, sejam realizadas, mesmo se uma exceção ocorrer no bloco `try`.

para finalizar essa seção será feito um programa que irá realizar cadastros de novos clientes. mais informações sobre o projeto [Projeto de Cadastramento]()