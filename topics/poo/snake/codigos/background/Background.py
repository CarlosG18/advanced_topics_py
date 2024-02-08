from .Element_back import Element_Back

class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matriz_elemet = []
        self.colunas = int(self.width/50)
        self.linhas = int(self.height/50)
        self.create()

    def create(self):
        for i in range(self.linhas):
            linha_matriz = []
            for j in range(self.colunas):
                if (j+i) % 2 == 0:
                    elemento = Element_Back(i,j,10+(j*50),10+(i*50),(0,255,0))
                    linha_matriz.append(elemento)
                else:
                    elemento = Element_Back(i,j,10+(j*50),10+(i*50),(0,150,0))
                    linha_matriz.append(elemento)

            self.matriz_elemet.append(linha_matriz)

    def show(self, screen):
        for element_linha in self.matriz_elemet:
            for element_coluna in element_linha:
                element_coluna.show(screen)

    def get_xy(self,i, j):
        return (self.matriz_elemet[i][j].x,self.matriz_elemet[i][j].y)