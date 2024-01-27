from .Element_back import Element_Back

class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.vetor_elemet = []
        self.create()

    def create(self):
        num_colunas = int(self.width/50)
        num_linhas = int(self.height/50)

        print(f'numero de linhas = {num_linhas}, numero de colunas = {num_colunas}')

        for i in range(num_linhas):
            linha_matriz = []
            for j in range(num_colunas):
                if (j+i) % 2 == 0:
                    elemento = Element_Back(i,j,i*50,j*50,(0,255,0))
                    linha_matriz.append(elemento)
                    print(f'i={i}, j={j}')
                else:
                    elemento = Element_Back(i,j,i*50,j*50,(0,150,0))
                    linha_matriz.append(elemento)
                    print(f'i={i}, j={j}')

            self.vetor_elemet.append(linha_matriz)

    def show(self, screen):
        for element_linha in self.vetor_elemet:
            for element_coluna in element_linha:
                element_coluna.show(screen)

    def print_element(self):
        for i in self.vetor_elemet:
            print(i)
            print('\n')