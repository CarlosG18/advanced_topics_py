from snake.Element import Element

class Bosters(Element):
    def __init__(self, url_img, x, y, i, j, function):
        super().__init__(url_img, x, y, i, j, None)
        self.function = function

class Imagem(Element):
    def __init__(self, url_img, x, y, width, height):
        super().__init__(url_img, x, y, None, None, None)
        self.width = width
        self.height = height
        self.create()

    def __str__(self):
        return f'imagem {self.url_img}'
