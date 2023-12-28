# Exercício de Iteradores em Python:

Suponha que você está trabalhando com uma lista de alunos e suas respectivas notas. Crie uma classe chamada RegistroNotas que implementa um iterador para percorrer as notas dos alunos. A classe deve ter os seguintes métodos:

__init__(self, alunos): Um construtor que recebe uma lista de alunos, onde cada aluno é representado por um dicionário com as chaves 'nome' e 'nota'. Exemplo: {'nome': 'Alice', 'nota': 85}.

__iter__(self): Retorna o objeto iterável (geralmente self).

__next__(self): Retorna a próxima nota do aluno a cada chamada. Se todas as notas foram percorridas, deve lançar a exceção StopIteration.

Crie uma instância da classe RegistroNotas com uma lista de pelo menos cinco alunos e suas notas. Em seguida, use um loop for para percorrer e exibir todas as notas dos alunos.

Lembre-se de incluir comentários no código para explicar cada parte da implementação.

**GERADO PELO CHATGPT**



