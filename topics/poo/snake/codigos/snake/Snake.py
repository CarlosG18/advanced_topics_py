from .Element import Head, Body, Tail

class Snake:
    def __init__(self, tamanho, velo):
        self.tamanho = tamanho
        self.velo = velo
        self.direcao = "left"
        self.corpo = []
        self.create_snake()

    def create_snake(self):
        cabeca = Head(0,0)
        self.corpo.append(cabeca)
        for i in range(1, self.tamanho):
            body = Body(i*50,0)
            self.corpo.append(body)
        rabo = Tail(self.tamanho*50,0)
        self.corpo.append(rabo)

    def move(self):
        if self.direcao == "left":
            for elemento in self.corpo:
                elemento.element_rect.x -= self.velo
        elif self.direcao == "right":
            for elemento in self.corpo:
                elemento.element_rect.x += self.velo
        elif self.direcao == "up":
            for elemento in self.corpo:
                elemento.element_rect.y -= self.velo
        elif self.direcao == "down":
            for elemento in self.corpo:
                elemento.element_rect.y += self.velo

    def show(self, screen):
        for element in self.corpo:
            element.show(screen)

    def move_top(self):
        self.direcao = "up"
    
    def move_left(self):
        self.direcao = "left"

    def move_down(self):
        self.direcao = "down"

    def move_right(self):
        self.direcao = "right"

    