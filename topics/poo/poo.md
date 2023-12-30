# Programação orientada a objetos

- aplicando os conceitos de poo em python na criação de um jogo com o pygame [dama](https://github.com/CarlosG18/advanced_topics_py/blob/main/topics/poo/dama/dama.md)

para criarmos classes em python usamos a palavra reservada `class`. na classe temos o **inicializador**, que será chamada toda vez que for feito uma instânciação, definindo os atributos padrões de cada objeto, dado pela função:

```python
def __init__(self):
    ...
```

o `self` receberá a instância do objeto. temos os atributos de classe, ao qual é definido fora da função `__init__()` e é aplicada quando esse atributo é geral para qualquer objeto dessa classe.

quando fazemos o print de um objeto, ele retornará um formato padrão do python que informa que tipo de objeto é seu endereço de memória. se quisermos alterá o formato podemos usar metodo:

```python
def __str__(self):
    return f'esse objeto possui o nome {self.nome}'
```

metódos que possuem as dois underline são chamados de metodos **dunder**.

## Herança

em python para definir uma herança basta colocar a classe pai dentro dos parenteses da classe filha, assim:

```python

class Animal():
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade

    def __str__(self):
        return f'animal com {self.altura} m e com {self.idade} anos de idade'

class Cachorro(Animal):
    def __init__(self):
        super().__init__()

```

voce pode acessar metodos da classe pai dentro de uma classe filha usando o `super()`