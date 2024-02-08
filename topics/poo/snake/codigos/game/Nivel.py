class Nivel:
    def __init__(self):
        self.nivel_atual = 1
        self.total_macas = self.qtd_maca_nivel()

    def qtd_maca_nivel(self):
        return 15*self.nivel_atual

    def snake_eat(self):
        self.total_macas -= 1

    def up_nivel(self):
        self.nivel_atual += 1
        self.total_macas = self.qtd_maca_nivel()

    def restart(self):
        self.nivel_atual = 1
        self.total_macas = self.qtd_maca_nivel()
