# Dama com Pygame

Para criarmos o jogo da dama precisamos de alguns elementos principais para a realização do jogo. são eles o **tabuleiro** e as **peças**.

## Tabuleiro

![Imagem do tabuleiro da Dama](https://github.com/CarlosG18/advanced_topics_py/blob/main/topics/poo/dama/imgs/tabuleiro_dama.jpg)

Inicialmente a estratégia que irei usar para a criação do tabuleiro será a seguinte:

- Irei criar uma classe para a **casa** do tabuleiro;
- analisando o tabuleiro, podemos abstrair para uma matriz 8x8;
- O **tabuleiro** em si será uma classe que conterá uma matriz de **casas** e mais alguns atributos relacionados ao jogo.

## Logica para a Dama

A lógica básica que eu usei para desenvolver o jogo, foi a seguinte:

Temos a classe **Casa** que possui o seguinte contrutor:

```python
class Casa:
  def __init__(self,i,j, x, y, width, height, color):
    self.i = i
    self.j = j
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.ocupado = None
    self.disponivel = False
    self.select = False
    self.color = color
    self.player = None
```
**aspectos importantes da classe Casa**:
- Como podemos observar, a casa possui os índicies para o respectivo valor da matriz (posição do tabuleiro);
- o atributo `disponivel` terá uma grande importância, pois será a partir dele que o jogo mostrará as possíveis casas que o jogador poderá jogar.
- o atributo `ocupado` receberá um objeto da classe **Peca**;

Temos também a classe `Tabuleiro`:

```python
class Tabuleiro:
  def __init__(self, tam, cor1, cor2):
    self.tam = tam
    self.cor1 = cor1
    self.cor2  = cor2
    self.casas_matriz = []
    self.casas_dispo = []
    self.matriz_pos = []
    self.tam_casa = None
    self.prox_jogada = 1
    self.casa_atual = None
    self.ajust_tam()
    self.create_casas()
    self.click = False
    self.peca_kill = None
    self.tag_kill = False
    self.priority = []
    self.modo_dama = []
```

**aspectos importantes dos atributos da classe Tabuleiro**:
- O atributo casas_matriz possui todas as casas do tabuleiro;
- O atributo prox_jogada define qual é o jogador que possui a prioridade para realizar a jogada;
- O atributo casa_atual guardará a peça que será selecionada pelo jogador;
- Os atributos peca_kill e tag_kill serão responsáveis por analisar se o jogador possui alguma peça a ser capturada;
- o vetor priority será usado para acrescentar as casas que possuem peças ao qual pela regra do jogo da dama deverá capturar obrigatoriamente;

## explicando o fluxo na classe Tabuleiro

A classe principal do jogo (Tabuleiro), contém tanto a criação de cada casa e peças dos jogadores como a lógica por trás do jogo. poderia ser criado uma nova classe como `Game` para desenvolver a lógica do jogo, porém por escolha própria foi decidido realizar tudo na classe `Tabuleiro`.

O fluxo acontece da seguinte maneira:

Tudo começa na função `check_click()`:
```python
def check_click(self, pos):
  i, j = self.get_casa_click(pos)
  casa = self.casas_matriz[i][j]

  if not self.casa_is_none(i,j) and casa.player == self.prox_jogada:
      if not (self.priority == []):
          for casa_p in self.priority:
              if casa.i == casa_p.i and casa.j == casa_p.j:
                  self.click_on(casa)
      else:
          self.click_on(casa)
  elif casa.disponivel:
      self.realizar_jogada(casa)
      if self.tag_kill:
          self.remove_peca_kill()
      self.check_continue_player(casa)
      self.check_priority(self.prox_jogada)
```

**resumindo**: esta função realiza a verificação se a casa do jogador é uma casa válida para mostrar as jogadas e se ela está dentro do vetor de prioridades, caso exista alguma casa no vetor de prioridades, nenhuma casa poderá ser escolhida a não ser a casa prioritária e com isso chamamos a função `click_on()` onde nela temos mais uma função importante que vale a pena comentar:

A função `show_jogadas()`:

```python
def show_jogadas(self, casa):
  #define se é player 1 (chave = 1) ou player 2 (chave = -1)
  if self.prox_jogada == 1:
      chave = 1
  else:
      chave = -1
  
  #primeira possibilidade: 1 caminho para a esquerda
  if casa.j+1 > 7:
      if not self.casa_is_none(casa.i+(1*chave),casa.j-1):
          if not self.casa_is_player(casa.i+(1*chave),casa.j-1):
              detalhes = self.check_kill(casa)
              if detalhes["kill"]:
                  self.tag_kill = True
                  self.peca_kill = self.casas_matriz[detalhes["kill_peca"]["i"]][detalhes["kill_peca"]["j"]]
                  for direcao in detalhes["directions"]:
                      i = direcao["i"]
                      j = direcao["j"]
                      self.activate_disponivel(i,j)
      else:
          self.activate_disponivel(casa.i+1*chave,casa.j-1)
  #segunda possibilidade: 1 caminho para a direita
  elif casa.j-1 < 0:
      if not self.casa_is_none(casa.i+(1*chave),casa.j+1):
          if not self.casa_is_player(casa.i+(1*chave),casa.j+1):
              detalhes = self.check_kill(casa)
              if detalhes["kill"]:
                  self.tag_kill = True
                  self.peca_kill = self.casas_matriz[detalhes["kill_peca"]["i"]][detalhes["kill_peca"]["j"]]
                  for direcao in detalhes["directions"]:
                      i = direcao["i"]
                      j = direcao["j"]
                      self.activate_disponivel(i,j)
      else:
          self.activate_disponivel(casa.i+(1*chave),casa.j+1)
  #terceira possibilidade: 2 caminhos (direita e esquerda)
  else:
      right, left = self.casas_prox_none(casa,chave)
      detalhes = self.check_kill(casa)

      if detalhes["kill"]:
          self.tag_kill = True
          self.peca_kill = self.casas_matriz[detalhes["kill_peca"]["i"]][detalhes["kill_peca"]["j"]]
          for direcao in detalhes["directions"]:
              i = direcao["i"]
              j = direcao["j"]
              self.activate_disponivel(i,j)
      else:    
          if not self.tag_kill and right:
              self.activate_disponivel(casa.i+(1*chave),casa.j+1)

          if not self.tag_kill and left:
              self.activate_disponivel(casa.i+(1*chave),casa.j-1)
```

**resumindo**: o que essa função faz é verificar os possíveis jogadas que a casa selecionada possui e caso tiver, as casas disponíveis serão ativadas (considere ativada como setando o atributo disponível e trocando a cor da casa para amarelo). essa verificação acontece em outra função `check_kill()` que retorna um dicionário que possui algumas informações sobre as casas que possuem peças a serem capturadas. atraves desses dados retornados pela função `check_kill()` podemos realizar a ativação das casas disponíveis.

De forma bem resumida, essa foi a minha estratégia para implemetar o jogo da dama. No momento pode ser uma solução não tão boa, pois não levantei aspectos como desenpenho, refatoração de código entre outros pontos.

## Bugs para reparar

- bug quando uma peça pode capturar duas peças ao mesmo tempo;
- bug em relação a peça a ser capturada quando a peça fez uma captura recente e possui duas possiveis peças para ele capturar, com o bug, o jogo não esta alterando a peça que será capturada.

## Futuras implementações

- Implementar a funçao da dama.
- Implementar o tempo para cada jogador.
- Implementar o ganhador do jogo.
- implementar o recomeçar.

