# Programação orientada a objetos

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

## Polimorfismo

o conceito de polimorfismo é dado quando temos ações diferentes para um mesmo nome de metodo de cada classe filha.

```python
class Personagem:
    def __init__(self, nome, idade, vida):
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def poder(self, poder):
        print(f'meu poder é {poder}')

    
class Mago(Personagem):
    def __init__(self, nome, idade, vida):
        super().__init__(nome, idade, vida)

    def poder(self):
        super().poder("bola de fogo")

class Guerreiro(Personagem):
    def __init__(self, nome, idade, vida):
        super().__init__(nome,idade,vida)

    def poder(self):
        super().poder("Força")


#instanciado um guerreiro e um mago:
mago = Mago("Gandof", 200, 200)
guerreiro = Guerreiro("Carlos", 500, 200)

mago.poder()
guerreiro.poder()
```

neste exemplo temos o mesmo metodo sendo chamado pelas classes filhas, porem o que irá modificar esse metodo será o objeto que irá chama-ló.

## Encapsulamento

O encapsulamento é a característica que um atributo possui de ser acessível ou não em diferentes partes do código. temos as seguintes formas:

- privados: atributos privados só podem ser alterados ou acessados através de metódos em sua própria classe; para fazer isso em python temos que usar a seguinte sintaxe:

```python
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

```

o atributo `nome` é um atributo público, ou seja, você consegue acessa-ló em qualquer lugar do seu código. já o atributo `cpf` por ser privado, você só conseguirá acessesa-ló atraves de metodos de sua classe. 

## Exercitando conceitos de POO

- aplicando os conceitos de poo em python na criação de um jogo com o pygame [dama](https://github.com/CarlosG18/advanced_topics_py/blob/main/topics/poo/dama/dama.md)
- aplicando os conceitos de poo em python na criação de um jogo com o pygame [SpaceFly](https://github.com/CarlosG18/advanced_topics_py/blob/main/topics/poo/spacefly/spacefly.md)