import os
class Pessoa:
    nome = 'Edu'
    idade = 21
    origem = 'BRA'

    def dizer_ola(self):
        print(f'Ola, eu sou {Pessoa.nome}')
    
    def pensar(self):
        print(f'Eu estou pensando!')

    def comprar(self):
        print(f'Compra realizada.')

    def get_nome(self):       
        return Pessoa.nome
    
    def get_idade(self):
        return Pessoa.idade

    def set_nome(self, nome_novo):
        Pessoa.nome = nome_novo
        

    def set_idade(self, idade_nova):
        Pessoa.idade = idade_nova




#Instanciando Objetos
pessoa_1 = Pessoa()
pessoa_2 = Pessoa()
# Chamando metodos da classe Pessoa via objetos
os.system('cls')  
pessoa_1.comprar()
pessoa_2.comprar()
pessoa_2.pensar()
pessoa_1.pensar()
# Chamando os getters
print(pessoa_1.get_nome())
print(pessoa_1.get_idade())
#Utilizando os setters
pessoa_1.set_nome('Ronaldinho')
print(pessoa_1.get_nome())
pessoa_2.set_idade(26)
print(pessoa_2.get_idade())