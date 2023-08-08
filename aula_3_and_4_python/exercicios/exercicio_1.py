# 1 - Classe Conta Bancária:
# Crie uma classe chamada ContaBancaria que simule uma conta bancária simples.
# A classe deve ter os atributos titular, saldo e numero. Crie métodos para depositar (depositar(valor))
# e sacar (sacar(valor)) dinheiro da conta, além de um método para exibir o saldo atual (exibir_saldo()).
import os


class ContaBancaria:
    titular = 'Eduardo Gehrke'
    saldo = 0
    numero = 1233257
    input_mensagem = 'Selecione a opcoes desejada'
    input_mensagem += '\n 1 - Depositar Valor'
    input_mensagem += '\n 2 - Sacar Valor'
    input_mensagem += '\n 3 - Exibir Saldo'
    input_mensagem += '\n 4 - Sair'


    
    def depositar_valor(valor):
        try:
            valor = float(valor)
            ContaBancaria.saldo += valor
        except:
            print('Informe um valor valido!')
    
    def sacar_valor(valor):
        try:
            valor = float(valor)
            ContaBancaria.saldo -= valor
        except:
            print('Informe um valor valido!')

    def exibir_saldo():
        print(f'Titular: {ContaBancaria.titular} com numero: {ContaBancaria.numero} e saldo: {ContaBancaria.saldo}')


    def script():
        while True:
            try:
                opcao = int(input(ContaBancaria.input_mensagem))
                if opcao == 1:
                    valor = input('Informe o valor: ')
                    ContaBancaria.depositar_valor(valor)
                elif opcao == 2:
                    valor = input('Informe o valor: ')
                    ContaBancaria.sacar_valor(valor)        
                elif opcao == 3:
                    ContaBancaria.exibir_saldo() 
                elif opcao == 4:
                    print('Volte sempre com dinheiro!')
                    break

            except KeyboardInterrupt:
                quit()
            except:
                print('Informe uma opcao valida!')
            





if __name__ == '__main__':
    ContaBancaria.script()

