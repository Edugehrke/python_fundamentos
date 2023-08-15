#1 - Crie uma classe abstrata chamada Animal com métodos falar(), comer() e mover().
#    Crie subclasses Cachorro, Cavalo e Gato que herdam da classe Animal e implementam
#    seus próprios métodos, printando frases diferentes.  
#    Crie e trabalhe com os getters e setters para as subclasses.
from abc import ABC, abstractmethod
import os

class AnimalAbstract(ABC):

    def __init__(self,especie, peso, cor,idade) -> None:
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.cor = cor



    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod 
    def comer(self):
        pass

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def exibir_informacoes(self):
        pass


class Cavalo(AnimalAbstract):

    def emitir_som(self):
        print('Prusssssss.. EEEEEHEHEHEHE')
   
    def comer(self):
        print('Comendo capim')

    def mover(self):
        print('Cavalgando')

    def exibir_informacoes(self):
        print(f'Especie: {self.especie} Peso: {self.peso} Cor: {self.cor} Idade: {self.idade}')



class Cachorro(AnimalAbstract):

    def emitir_som(self):
        print('Au au')

    def comer(self):
        print('qualquer coisa')

    def mover(self):
        print('PEGA PEGA')

    def exibir_informacoes(self):
        print(f'Especie: {self.especie} Peso: {self.peso} Cor: {self.cor} Idade: {self.idade}')


class Gato(AnimalAbstract):

    def emitir_som(self):
        print('Miau miau')

    def comer(self):
        print('Comeendo racao')

    def mover(self):
        print('Saltitando')

    def exibir_informacoes(self):
        print(f'Especie: {self.especie} Peso: {self.peso} Cor: {self.cor} Idade: {self.idade}')


if __name__ == '__main__':
    
    Cavalo_1 = Cavalo(
        especie = 'Machador', 
        idade = 10, 
        peso = 155.50, 
        cor = 'Marrom')
    

    Cavalo_2 = Cavalo(
        especie = 'Mustang', 
        idade = 3, 
        peso = 90.2, 
        cor = 'Preto')
        
    gato_objeto = Gato(
        especie = 'Ciames',
        idade = 6,
        peso = 2.5,
        cor = 'laranja'
    )

    cao_objeto = Cachorro(
        especie = 'Vira-lata',
        idade = 10,
        peso = 9.2,
        cor = 'Preto'
    )

Cavalo_1.exibir_informacoes()
Cavalo_2.exibir_informacoes()
gato_objeto.exibir_informacoes()
cao_objeto.exibir_informacoes()








