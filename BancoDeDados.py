import mysql.connector as mys
from Fabricante import *
from classe_estoque import *


class Data:
    def __init__(self):
        self.database = mys.connect(host='localhost', user='root', password='q1w2e3', database='banco')
        self.cursor = self.database.cursor()

    def cadastro_produto(self, nome, quant, fabri):
        self.cursor.execute('select cod from Fabricantes')
        veri = self.cursor.fetchall()

        for cod in veri:
            if fabri == cod[0]:
                produto = Produto(nome, quant, fabri)
                self.cursor.execute(f'insert into Produtos (descricao, quantidade, codigo_fabri) '
                                f'values ("{produto.desc}", "{produto.quant}", "{produto.fab}")')
                self.database.commit()

    def cadastro_fabricante(self, nome):
        fabricante = Salvar_Fabricante(nome)
        self.cursor.execute(f'insert into fabricante (nome) values ("{fabricante.nome}")')
        self.database.commit()

    def listar(self):
        self.cursor.execute('select Produtos.id, Produtos.descricao,Produtos.quantidade, Fabricantes.nome '
                        'from Produtos, Fabricantes where Fabricantes.cod = Produtos.cod_fabricantes')
        produtos = self.cursor.fetchall()
        for prod in produtos:
            print(70 * '\033[34m=', '\033[m')
            print(f'codigo: {prod[0]}'
              f'\nproduto: {prod[1]}'
              f'\nquantidade: {prod[2]}'
              f'\nfabricante: {prod[3]}')

    def altera_produtos(self, cod, mudar, valor):
        try:
            self.cursor.execute(f'update Produtos set {mudar} = "{valor}" where id = {cod}')
            self.database.commit()
        except:
            print('codigo não encontrado')
