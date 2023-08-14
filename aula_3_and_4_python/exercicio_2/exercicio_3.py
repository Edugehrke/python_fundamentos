#        3- - Classe Conta Bancária:
#        Crie uma classe chamada ContaBancaria, com os atributos saldo (private), titular (public), numero_conta (private). Crie métodos get_saldo() e
#        set_saldo(novo_saldo) para acessar e modificar o saldo.

import os

class ContaBancaria:

    def __init__(self,saldo,titular,numero_conta) -> None:
        self.__saldo = saldo
        self.titular = titular
        self.__numero_conta = numero_conta


    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,saldo_novo):
        self.__saldo = saldo_novo




if __name__ == '__main__':
    os.system('cls')
    conta_1 = ContaBancaria(100,'bruno', 15)
    conta_2 = ContaBancaria(200,'bruna', 23)

    print(conta_1.titular)
    print(conta_1.saldo)
    print(conta_2.titular)
    print(conta_2.saldo)
    print('\n')

    conta_1.saldo = 500
    conta_2.saldo = 7020

    print(conta_1.titular)
    print(conta_1.saldo)
    print(conta_2.titular)
    print(conta_2.saldo)
