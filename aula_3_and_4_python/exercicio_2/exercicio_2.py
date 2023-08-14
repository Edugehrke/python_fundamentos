#2 - Classe Pessoa:
#   Crie uma classe chamada Pessoa com o atributo nome (public). 
#   Implemente métodos set_nome(novo_nome) e get_nome() para manipular esse atributo.
import os

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome_novo):
        self.nome = nome_novo



if __name__ == '__main__':
    os.system('cls')
    pessoa_1 = Pessoa('Caue')
    pessoa_2 = Pessoa('Edu')
    pessoa_3 = Pessoa('Ola')

    print(pessoa_1.get_nome())
    print(pessoa_2.get_nome())
    print(pessoa_3.get_nome())

    pessoa_1.set_nome('mr_robot')
    pessoa_2.set_nome('mr_robot')
    pessoa_3.set_nome('mr_robot')

    print(pessoa_1.get_nome())
    print(pessoa_2.get_nome())
    print(pessoa_3.get_nome())
