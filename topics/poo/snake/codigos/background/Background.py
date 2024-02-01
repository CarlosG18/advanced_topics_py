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
        #print(f'numero de linhas = {num_linhas}, numero de colunas = {num_colunas}')
        for i in range(self.linhas):
            linha_matriz = []
            for j in range(self.colunas):
                if (j+i) % 2 == 0:
                    elemento = Element_Back(i,j,10+(j*50),10+(i*50),(0,255,0))
                    linha_matriz.append(elemento)
                    #print(f'i={i}, j={j}')
                else:
                    elemento = Element_Back(i,j,10+(j*50),10+(i*50),(0,150,0))
                    linha_matriz.append(elemento)
                    #print(f'i={i}, j={j}')

            self.matriz_elemet.append(linha_matriz)
        #print(self.print_element())

    def show(self, screen):
        for element_linha in self.matriz_elemet:
            for element_coluna in element_linha:
                element_coluna.show(screen)

    def print_element(self):
        for i in self.matriz_elemet:
            for elemento in i:
                print(elemento)

    def get_xy(self,i, j):
        return (self.matriz_elemet[i][j].x,self.matriz_elemet[i][j].y)