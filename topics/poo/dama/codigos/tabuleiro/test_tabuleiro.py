from .tabuleiro import Tabuleiro

@pytest.fixture
def tabuleiro_inicial():
  return Tabuleiro(1280,(0,153,0),(200,0,0))
  
def test_show_jogadas(tabuleiro_inicial):
    # Defina o estado inicial ou forneça os valores necessários
    casa_inicial = tabuleiro_inicial.casas_matriz[0][1]
    detalhes = {"activate": True, "direction": "right"}

    # Execute a função que você deseja testar
    tabuleiro_inicial.show_jogadas(casa_inicial, detalhes)

    # Adicione asserções para verificar se o resultado é o esperado
    assert casa_inicial.player == 1
    # Certifique-se de incluir asserções apropriadas para o seu caso

  