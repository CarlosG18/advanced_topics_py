class Personagem:
    def __init__(self, nome, idade, vida):
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def poder(self, poder):
        print(f'meu poder é {poder}')

    
class Mago(Personagem):
    def __init__(self, nome, idade, vida):
        super().__init__(nome, idade, vida)

    def poder(self):
        super().poder("bola de fogo")

class Guerreiro(Personagem):
    def __init__(self, nome, idade, vida):
        super().__init__(nome,idade,vida)

    def poder(self):
        super().poder("Força")


#instanciado um guerreiro e um mago:
mago = Mago("Gandof", 200, 200)
guerreiro = Guerreiro("Carlos", 500, 200)

mago.poder()
guerreiro.poder()