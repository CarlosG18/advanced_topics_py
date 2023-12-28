# Iterators

iteradores são objetos que possuem um número contaveis de valores. esse objeto possui duas funcões principais: 

- iter(): ao qual transforma um dado em um objeto iterador.
- next(): que obtém o proximo elemento do iterador.

o funcionamento do `for` no python funciona através do iterator, onde se usa o `next()` para realizar o for.

para definir uma classe que possua um objeto com o iterador devemos criar as seguintes funções:

```python
def __iter__(self):
  #logica do iterador
  
def __next__(self):
  #logica do proximo elemento
```

podemos usar uma palavra reservada para evitar infinitas repetições, caso a sua aplicação nescessite. usamos o `StopIteration`

- [exercicio de iterators]()