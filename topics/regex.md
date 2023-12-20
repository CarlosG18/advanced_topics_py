# RegEx in Python

Expressões regulares são uma forma de verificar se uma string está dentro de um determinado padrão. para usarmos em **python** devemos usar a lib **re**:

```python
import re

```

para criarmos um padrao podemos ultilizar o metodo **compile()**.

# sintaxe do RegEx

para criarmos os padroes que precisamos, precisamos usar a sintaxe do RegEx. alguns elementos básicos são:

-   "." : qualquer caractere pode estar naquele lugar;
-   "^" : especificar o que deve ter no inicio da string;
-   "$" : especificar o que deve ter no final da string;
-   "*" : ou tem 0 ou muitos;
-   "+" : ou tem 1 ou muitos;
-   "?" : ou tem 0 ou tem 1;
-   []  : indica um conjunto de caracteres;
-   {3} : informar a quantidade de vezes que um determinado padrão deve ocorrer;
-   {x,y} : informar o minimo x e o maximo y em que o padrão ocorre.

## tarefas 

- [regex para email]()
- [regex para cpf]()
- [regex para senhas]()