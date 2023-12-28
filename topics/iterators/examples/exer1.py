#respondendo o exercicio
class RegistroNotas:
  def __init__(self, alunos):
    self.alunos = alunos
    
  def __iter__(self):
    self.index = 0
    return self
    
  def __next__(self):
    if self.index < len(self.alunos):
      self.aluno = self.alunos[self.index]
      self.index += 1
      return self.aluno["nota"]
    else:
      raise StopIteration

alunos = [
    {"aluno": "zeca" , "nota": 8.9},
    {"aluno": "pedro", "nota": 7.8},
    {"aluno": "carlos", "nota": 10},
    {"aluno": "matheus", "nota": 8.6},
    {"aluno": "jean", "nota": 9.0},
  ]
  
regNota = RegistroNotas(alunos)

for nota in regNota:
  print(nota)