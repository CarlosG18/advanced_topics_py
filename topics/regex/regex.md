# RegEx in Python

Expressões regulares são uma forma de verificar se uma string está dentro de um determinado padrão. para usarmos em **python** devemos usar a lib **re**:

```python
import re

```

para criarmos um padrao podemos ultilizar o metodo **compile()**.

## sintaxe do RegEx

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

## algumas funções da lib re



## tarefas 

- [regex para email](https://github.com/CarlosG18/advanced_topics_py/blob/main/topics/regex/email.md)
- [regex para cpf](https://github.com/CarlosG18/advanced_topics_py/blob/main/topics/regex/cpf.md)
- [regex para senhas](https://github.com/CarlosG18/advanced_topics_py/blob/main/topics/regex/senha.md)