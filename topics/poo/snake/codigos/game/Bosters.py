from snake.Element import Element

class Bosters(Element):
    def __init__(self, url_img, x, y, i, j, function):
        super().__init__(url_img, x, y, i, j, None)
        self.function = function