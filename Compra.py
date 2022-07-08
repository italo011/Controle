from classe_estoque import *


class Compra:
    def __init__(self):
        self.sus = Estoque()

    def comprar(self):
        controle = int(input('Informe o código do produto:\n'))
        for i in range(len(self.sus.puxar)):
            if controle == self.sus.puxar[i].cod:
                self.sus.puxar[i].quant += \
                    int(input('Informe a quantidade comprada:\n'))
            else:
                pass