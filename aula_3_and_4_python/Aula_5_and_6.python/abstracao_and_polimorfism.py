
from abc import ABC, abstractmethod
import os

class PessoaAbstrata(ABC):

    @abstractmethod
    def gastar_dinheiro():
        pass


    @abstractmethod
    def respirar():
        pass

    @abstractmethod
    def falar():
        pass



class Atleta(PessoaAbstrata):
    def gastar_dinheiro():
        print('Eu gasto pouco dinheiro!')

    def falar():
        print('Queremos um aumento!')

    def respirar():
        print('Respiro 2 e inspiro 1')


class Artista(PessoaAbstrata):
    def gastar_dinheiro():
        print('Eu gasto muito dinheiro!')   

    
    def falar():
        print('Eu sou rico e falo 5 idiomas!')

    def respirar():
        print('Sou pago até para respeirar! ')


os.system('cls')
Atleta.gastar_dinheiro()
Atleta.falar()
Atleta.respirar()
print('\n')
Artista.gastar_dinheiro()
Artista.falar()
Artista.respirar()