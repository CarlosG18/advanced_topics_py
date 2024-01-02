import math

def soma(a, b):
  return a + b
  
def div(a,b):
  if b == 0:
    raise ValueError("divisor não pode ser 0")
  return a/b
  
def test_soma():
  assert soma(0,5) == 5
  assert soma(1,-1) == 0
  
def test_div():
  assert div(0,2) == 0
  assert div(2,2) == 1
  assert div(-10,2) == -5
  
  try:
    div(9,0)
  except ValueError as e:
    assert str(e) == "divisor não pode ser 0"
  else:
    assert False, "falha"
    
  
  
  
  
  