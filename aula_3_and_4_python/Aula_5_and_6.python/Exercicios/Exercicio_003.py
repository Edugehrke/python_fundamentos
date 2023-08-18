#3 - Crie uma classe base Veiculo com atributos como marca, modelo e métodos como ligar()
#    e desligar(), entre outros. Crie as subclasses Carro e Moto que herdam de Veiculo e
#    implementam seus próprios métodos beaseando-se na abstratação de Veiculo. Em seguida,
#    crie uma classe Garagem que aceita veículos e gerencia o estacionamento usando herança.
#    Crie e trabalhe com os getters e setters para a classe Garagem.


from abc import ABC, abstractmethod


class Veiculo(ABC):

    def __init__(self, marca, modelo, ligado) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ligado = ligado



    @abstractmethod
    def ligar(self):
        pass

    
    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def ligar(self):
        if self.ligado == True:
            print('O Carro já esta ligado')
        else:
            self.ligado = True
            print('Carro ligado com sucesso!')

    def desligar(self):
        if self.ligado == False:
            print('O Carro já esta desligado')
        else:
            self.ligado = False
            print('Carro desligado com sucesso!')




class Moto(Veiculo):
    def ligar(self):
        if self.ligado == True:
            print('A moto já esta ligada')
        else:
            self.ligado = True
            print('Moto ligada com sucesso!')


    def desligar(self):
        if self.ligado == False:
            print('A moto já esta desligada')
        else:
            self.ligado = False
            print('Moto desligada com sucesso!')



class Garagem():
    def __init__(self) -> None:
        self.veiculos_estacionados = []


    def estacionar(self, auto_nome):
        self.veiculos_estacionados.append(auto_nome)
        print(f'Veiculo {auto_nome} Estacionado com sucesso!')

    
    def mostra_auto_estacionados(self):
        if len(self.veiculos_estacionados) > 0:
            print('Garagem:')
            for indice,veiculo in enumerate(self.veiculos_estacionados):
                print(f'Veiculo {indice + 1}: {veiculo} ')
        else:
            print('Ainda nao existem veiculos na garagem!')


moto_objeto = Moto('Honda','Hornet',False)
carro_objeto = Carro('Fiat','Palio',False)

print(moto_objeto.marca)
print(moto_objeto.modelo)
moto_objeto.desligar()
moto_objeto.ligar()

print('\n')

print(carro_objeto.marca)
print(carro_objeto.modelo)
carro_objeto.desligar()
carro_objeto.ligar()


print('\n')

garagem_objeto = Garagem()
garagem_objeto.mostra_auto_estacionados()

garagem_objeto.estacionar(f'Carro aleatorio -  {carro_objeto.marca}')
garagem_objeto.estacionar(f'Carro aleatorio 2  -  {carro_objeto.marca}')


garagem_objeto.estacionar(f'moto aleatorio -  {moto_objeto.marca}')
garagem_objeto.estacionar(f'moto aleatorio 2  -  {moto_objeto.marca}')

garagem_objeto.mostra_auto_estacionados()