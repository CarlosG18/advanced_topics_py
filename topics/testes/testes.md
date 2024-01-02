# Testes em Python com o pytest

- se você não informar o arquivo explicitamente, o pytest executará os arquivos do diretorio atual e subdiretorios que possuirem o formato **teste_*.py** ou ***_test.py**.

- as funçoes de teste devem começar com **test**

- para criar um possivel teste voce deveerá usar a palavra reservada `assert`, nisso voce deve passar o que seria uma possivel chamada da função e em seguida o valor em que deveria ser obtido.

para executar os testes em todos os arquivos de testes basta executar o seguinte comando: 

```bash
$ pytest -v
```

caso apenas um arquivo de testes deve ser executado usamos:

```bash
$ pytest <nome_do_arquivo> -v
```

## executando um subgrupo de testes

podemos usar esse comando:

```bash
$ pytest -k <palavra> -v
```

para executar testes que possuem a palavra em seu nome: test_**palavra**()
