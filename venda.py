from Compra import *


class Venda:
    def __init__(self):
        self.vivo = Estoque()

    def vender(self):
        controle_venda = int(input('Informe o código do produto:\n'))
        for i in range(len(self.vivo.puxar)):
            if controle_venda == self.vivo.puxar[i].cod:
                self.vivo.puxar[i].quant -= \
                    int(input('Informe a quantidade a vender:\n'))
            else:
                pass