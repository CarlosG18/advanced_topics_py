from .tabuleiro import Tabuleiro
import pytest

@pytest.fixture
def tabuleiro_inicial():
  return Tabuleiro(1280,(0,153,0),(200,0,0))
  
def test_show_jogadas(tabuleiro_inicial):
    #caso 1 - quina esquerdo
    casa_inicial = tabuleiro_inicial.casas_matriz[1][0]
    detalhes = {"activate": False, "direction": None}
    tabuleiro_inicial.show_jogadas(casa_inicial, detalhes)
    assert tabuleiro_inicial.casas_matriz[casa_inicial.i+1][casa_inicial.j+1].disponivel == False

    #caso 2 - quina direita
    casa_inicial = tabuleiro_inicial.casas_matriz[0][7]
    detalhes = {"activate": False, "direction": None}
    tabuleiro_inicial.show_jogadas(casa_inicial, detalhes)
    assert tabuleiro_inicial.casas_matriz[casa_inicial.i+1][casa_inicial.j-1].disponivel == False

    #caso 3 - peca sem movimentos
    casa_inicial = tabuleiro_inicial.casas_matriz[1][2]
    detalhes = {"activate": False, "direction": None}
    tabuleiro_inicial.show_jogadas(casa_inicial, detalhes)
    assert tabuleiro_inicial.casas_matriz[casa_inicial.i+1][casa_inicial.j+1].disponivel == False and tabuleiro_inicial.casas_matriz[casa_inicial.i+1][casa_inicial.j-1].disponivel == False
