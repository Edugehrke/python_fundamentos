import os
class Animal:
#--------------------- CONSTRUTOR ---------------------

    # PRIVATE -> __nome
    # PROTECTED -> _nome
    # PUBLIC - nome

    os.system('cls')
    def __init__(self, raca, cor, idade,nome):
        self._raca = raca # protected
        self._cor = cor # protected
        self._idade = idade # protected
        self.__nome = nome # private 
        print('Objeto instanciado com sucesso!')



#--------------------- GETTERS ----------------------
    @property
    def raca(self):
        return 'Raca ->'+ self._raca

    @property
    def cor(self):
        return 'Cor -> '+ self._cor

    @property
    def idade(self):
        return f'Idade -> {self._idade}'
    
    @property
    def nome(self):
        return f'Nome -> {self.__nome}'
    
    
    
#---------------------- SETTER ----------------------

    @raca.setter
    def raca(self, raca_nova):
        print(f'Setou  {self.raca} para {raca_nova}')
        self._raca = raca_nova

    @cor.setter
    def cor(self, cor_nova):
        print(f'Setou  {self.cor} para {cor_nova}')
        self._cor = cor_nova

    @idade.setter
    def idade(self, idade_nova):
        print(f'Setou  {self.idade} para {idade_nova}')
        self._idade = idade_nova


    @nome.setter
    def nome(self, nome_novo):
        print(f'Setou {self.__nome} para {nome_novo}')
        self.__nome = nome_novo



if __name__ == '__main__':
    
#---------------------- Instancias (CRIACOES) DOS OBJETOS DA CLASSE ANIMAL ----------------------
    leao = Animal('leao da montanha', 'preto', 15,'simba')
    gato = Animal('gato', 'branco',11,'xivano')
    pantera = Animal('pantera ','rosa',21,'king')
#---------------------- UTILIZAR GETTS PARA CADA OBJETO ----------------------
    print('')
    print(leao.raca)
    print(leao.cor)
    print(leao.idade)
    print('')
    print(gato.raca)
    print(gato.cor)
    print(gato.idade)
    print('')
    print(pantera.raca)
    print(pantera.cor)
    print(pantera.idade)

    pantera.idade = 56
    pantera.cor = 'verde'
    gato.raca = 'persa'

    print(pantera.nome)

