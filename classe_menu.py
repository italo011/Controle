from Compra import Compra
from classe_estoque import Estoque
from venda import *
from Fabricante import *
class Menu:
    def __init__(self):
        self.ai = Estoque()
        compra = Compra()
        compra.sus = self.ai
        venda = venda()
        venda.vivo = self.ai
        self.fabrica = Fabricante()
        self.ai.entrada = self.fabrica
        while True:
            entrada = input('1-Cadastrar\n2-Listar\n3-Trocar Produto\n4-Comprar\n5-Vender\n6-Cadastrar Fabricante\n7-Sair:\n')
            print(80 * '\033[34m=', '\033[m')
            if entrada == '1':
                self.ai.salvar_produtos()
            elif entrada == '2':
                self.ai.listar_produtos()
            elif entrada == '3':
                self.ai.trocar_produto()
            elif entrada == '4':
                compra.comprar()
            elif entrada == '5':
                venda.vender()
            elif entrada == '6':
                self.fabrica.cadastrar()
            elif entrada == '7':
                break