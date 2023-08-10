#        3 - Classe Carro:
#       Crie uma classe chamada Carro que simule um carro. A classe deve ter os atributos marca, modelo e ano.
#       Crie métodos para ligar (ligar()), desligar (desligar()) e exibir as informações do carro (exibir_informacoes()).


class Carro:
    marca = 'Renault'
    modelo = 'Sandero'
    ano = 2021


    def ligar():
        print('O carro ligou')
    
    def desligar():
        print('O carro desligou')

    def exibe_infor():
        print(Carro.marca, Carro.modelo, Carro.ano)



if __name__ == '__main__':  
    Carro.exibe_infor()