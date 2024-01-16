# Functions Lambda

funções lambda são funções em python que não precisam de uma definição `def`. elas recebem argumentos e retornam expressões únicas. seu formato é dado da seguinte maneira:

```python
lambda argumentos : expressao
```

podemos nomear uma função lambda:

```python
num_duplicado = lambda x : x * 2
num_duplicado(2)
```

podemos tambem usar funções lambdas como funções de ordem superior, ao qual recebem como argumentos um ou mais funções e retornam uma ou mais funções. exemplo:

```python
func_quadratica = lambda x, func : x * x + func(x+2)
func_quadratica(2,lambda x : x / 2)
```

explicando o codigo acima:

