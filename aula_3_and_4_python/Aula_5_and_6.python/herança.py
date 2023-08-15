import os
#Parent CLASS
class Animal:
    def __init__(self,nome, cor) -> None:
        self.nome = nome 
        self.cor = cor


    def correr(self):
        print(f'{self.nome} está correndo...')


    def comer(self):
        print(f'{self.nome} está se alimentando...')


#Sub-classe herando a classe ANIMAL***
class Cachorro(Animal):
    def latir(self):
        print('Au au - I am a dog')

    


class Gato(Animal):

    def destruir_sofa(self):
        print('Sofa foi de base')

    def miar(self):
        print('meau meau')


if __name__ == '__main__':
    os.system('cls')

    cao_1 = Cachorro('brian','black')
    cao_1.comer()
    cao_1.correr()
    cao_1.latir()

    gato_1 = Gato('vixano','white')
    gato_1.comer()
    gato_1.correr()
    gato_1.destruir_sofa()
    gato_1.miar()