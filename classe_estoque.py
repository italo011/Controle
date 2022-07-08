from produto import *
from Fabricante import *

class Estoque:
    def __init__(self):
        self.puxar = []
        self.puxar.append(Produto(1, 'Lapis', 'aa', 0))
        self.entrada = Fabricante()


    def salvar_produtos(self):
        entrada_cod = int(input('Informe o codigo:\n'))
        entrada_desc = input('Informe a descricao:\n')
        entrada_quant = int(input('Informe a quantidade:\n'))
        fra = int(input('informe o codigo do fabricante:\n'))
        for fabri in range(len(self.entrada.fab)):
            if fra == int(self.entrada.fab[fabri].cod):
                self.puxar.append(Produto(cod=entrada_cod, desc=entrada_desc, fab = self.entrada.fab[fabri].nome, quant=entrada_quant))
                print('Produto salvo')
            else:
                print('Fabricante desconhecido.')


    def listar_produtos(self):
        for i in range(len(self.puxar)):
            print('Cod:\n', self.puxar[i].cod, '\nDescrição:\n', self.puxar[i].desc, '\nFabricante:\n', self.puxar[i].fab, '\nQuantidade\n',
                  self.puxar[i].quant)

    def trocar_produto(self):
        coloca = input('Informe o codigo do produto:\n')
        for i in range(len(self.puxar)):
            if coloca == self.puxar[i].cod:
                self.puxar[i].desc = input('Digite a descrição nova:\n')