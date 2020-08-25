class Aviao():
    def __init__(self, cor, tipo, empresa):
        
        self.cor = cor
        self.tipo = tipo
        self.empresa = empresa

    def voar(self):
        self.empresa = input('Digite o nome da empresa de aviação: ')
        print('\n')
        print(self.tipo +' da '+self.empresa+' '+self.cor + ' esta Voando')

    def pousar(self):
        print('Agora '+self.tipo +' da ' +self.empresa +' '+ self.cor + ' esta Pousando')