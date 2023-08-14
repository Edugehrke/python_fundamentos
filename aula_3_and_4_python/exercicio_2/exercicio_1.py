 #       1 - Classe Produto:
 #       Crie uma classe chamada Produto que represente um produto em uma loja. A classe deve ter os atributos: nome (private), preco
 #       e codigo (public). Crie um construtor para inicializar esses atributos e métodos get_nome(), get_preco() e set_preco(novo_preco) para
 #       acessar e modificar o preço.

import os

class Produto:

    def __init__(self, nome, preco, codigo):
        self.__nome = nome
        self.preco = preco
        self.codigo = codigo



#--------------------- GETTERS ----------------------
    @property
    def nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.preco
#--------------------- SETTERS ----------------------
    def set_preco(self, preco_novo):
        self.preco = preco_novo


if __name__ == '__main__':
    carro_objeto = Produto('carro', 20000, 1435465)
    os.system('cls')

    print(carro_objeto.nome)

    print(carro_objeto.get_preco())



