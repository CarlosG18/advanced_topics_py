# Dama com Pygame

para criarmos o jogo da dama precisamos de alguns elementos principais para a realização do jogo. são eles o **tabuleiro** e as **peças**.

## Tabuleiro

![Imagem do tabuleiro da Dama](https://github.com/CarlosG18/advanced_topics_py/blob/main/topics/poo/dama/imgs/tabuleiro_dama.jpg)

inicialmente a estrategia que irei usar para a criação do tabuleiro será a seguinte:

- Irei criar uma classe para a **casa** do tabuleiro;
- O **tabuleiro** será uma classe que conterá uma matriz de **casas** e mais alguns atributos relacionados ao jogo.

## Bugs para reparar

- A peça esta capturando para "tras";
- bug quando uma peça pode capturar duas peças ao mesmo tempo;
- bug em relação a peça a ser capturada quando a peça fez uma captura recente e possui duas possiveis peças para ele capturar, com o bug, o jogo não esta alterando a peça que será capturada.
- indicie fora do range da matriz das casas **done**:

```bash
Traceback (most recent call last):
  File "/home/car/carlos/roadmaps/python/advanced_topics_py/topics/poo/dama/codigos/main.py", line 50, in <module>
    tabuleiro.check_click(pygame.mouse.get_pos())
  File "/home/car/carlos/roadmaps/python/advanced_topics_py/topics/poo/dama/codigos/tabuleiro/tabuleiro.py", line 252, in check_click
    self.click_on(casa)
  File "/home/car/carlos/roadmaps/python/advanced_topics_py/topics/poo/dama/codigos/tabuleiro/tabuleiro.py", line 231, in click_on
    self.show_jogadas(casa)
  File "/home/car/carlos/roadmaps/python/advanced_topics_py/topics/poo/dama/codigos/tabuleiro/tabuleiro.py", line 288, in show_jogadas
    if not self.casa_is_none(casa.i+(1*chave),casa.j+1):
  File "/home/car/carlos/roadmaps/python/advanced_topics_py/topics/poo/dama/codigos/tabuleiro/tabuleiro.py", line 323, in casa_is_none
    if self.casas_matriz[i][j].ocupado == None:
IndexError: list index out of range
```

## Futuras implementações

- Implementar a funçao da dama.
- Implementar o tempo para cada jogador.
- Implementar o ganhador do jogo.
- implementar o recomeçar.

