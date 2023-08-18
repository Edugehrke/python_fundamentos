#2 - Crie uma classe Banco com métodos abstratos depositar(), ver_saldo() e sacar() e 
#implemente a lógica de cada método. Crie subclasses ContaCorrente e ContaPoupanca
#que herdam da classe Banco e implementam os métodos de acordo com suas regras específicas.
#Por exemplo, a subclasse ContaPoupanca pode nao deter o método sacar().
#Crie atributos privados e publicos nas subclasses ContaCorrente e ContaPoupanca
#como self.nome, self.saldo, e self.numero_conta por exemplo. Crie objetos dessas
#classes com informações distintas, invoque os métodos e printe o resultado das
#operações. 

from abc import ABC, abstractmethod
import os


class Banco(ABC):

    def __init__(self,nome,saldo,numero_conta) -> None:
        self.nome = nome 
        self.saldo = saldo
        self.numero_conta = numero_conta

    def get_nome(self):
        pass

    def get_saldo():
        pass

    def numero_conta():
        pass

    def set_saldo():
        pass




class ContaCorrente(Banco):

    def exibir_informacoes(self):
        print(f'O seu nome é {self.nome} seu saldo atual é: {self.saldo} e o numero da sua conta:{self.numero_conta} ')

    def set_nome(self,nome_novo):
        self.nome = nome_novo


    def get_nome(self):
        return self.nome
    

    

class ContaPoupanca(Banco):
    def exibir_informacoes(self):
        print(f'O seu nome é {self.nome} seu saldo atual é: {self.saldo} e o numero da sua conta:{self.numero_conta} ')

    def set_saldo(self, saldo_novo):
        self.saldo = saldo_novo

    def set_nome(self, nome_novo):
        self.nome = nome_novo

    def get_saldo(self):
        return self.saldo
    
    def get_nome(self):
        return self.nome
    
    
if __name__ == '__main__':
    os.system('cls')
    while True:
        try:
            opcao = input('--------digite (1) para sua CONTA POUPANCA--------\n --------digite (2) para sua CONTA CORRENTE--------')
            if opcao == '1':
                nome = input('Digite seu nome: ')
                conta_1 = ContaCorrente(nome,0,12121)
                print(conta_1.exibir_informacoes())
                print('\n')
                opcao_2 = input('Informe a opcao que voce deseja realizar? \n ---------------(1) Adicionar SALDO \n (2) SAIR \n (3) Alterar nome')
                if opcao_2 == '1':
                    ...
                


        except Exception as e:
            print('error')

    

