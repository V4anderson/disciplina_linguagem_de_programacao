class TimeFutebol():
    def __init__(self, nome, tipo, cidade):
        self.nome = nome
        self.tipo = tipo
        self.cidade = cidade
    
    def ganhou(self,adversario):
        print(self.nome + ' Ganhou o jogo de 1 x 0 para o '+adversario)

    def perdeu(self,adversario):
        print(self.nome + ' Perdeu o jogo de 1 x 0 para o '+adversario)