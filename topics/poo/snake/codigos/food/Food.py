from snake.Element import Element

class Food(Element):
    def __init__(self,url_img, x, y, i, j):
        return super().__init__(url_img, x, y, i, j, None)
