import os

class Calculator:
    operacoes_limite = 10
    input_mensagem  = '1 = Somar'
    input_mensagem += '\n2 = Subtrair'
    input_mensagem += '\n3 = Multiplicar'
    input_mensagem += '\n4 = Dividir'
    input_mensagem += '\n5 = Modulo'
    input_mensagem += '\n6 = Sair'
    input_mensagem += '\nInforme a operacao: '

    def somar(numero_1, numero_2): 
        print(f'\33[032m A soma é: {numero_1 + numero_2} \33[0m')
        
    
    def subtrair(numero_1, numero_2):
        print(f'\33[032m Substracao = {numero_1 - numero_2} \33[0m')
        
    def mult(numero_1, numero_2):
        print(f'\33[032m Multiplicacao = {numero_1 * numero_2} \33[0m')
    
    def dividir(numero_1, numero_2):
        print(f'\33[032m Divisao:  {numero_1/numero_2} \33[0m')
    
    def modulo(numero_1, numero_2):
        print(f'\33[032m Resto-div: {numero_1%numero_2} \33[0m ')
    
    def controle_operacoes():
        contador = 0
        while contador < Calculator.operacoes_limite:
            contador += 1      
            try:
                numero_1 = int(input('Informe o primeiro numero: '))
                numero_2 = int(input('Informe o segundo numero: '))

                if numero_1 > 0 and numero_2 > 0:                    
                    while True:
                        try:
                            opcao = int(input(Calculator.input_mensagem))                               
                            if opcao == 1:
                                Calculator.somar(numero_1, numero_2)
                                
                            elif opcao == 2:
                                Calculator.subtrair(numero_1, numero_2)
                                
                            elif opcao == 3:
                                Calculator.mult(numero_1, numero_2)
                                
                            elif opcao == 4:
                                Calculator.dividir(numero_1, numero_2)
                                
                            elif opcao == 5:
                                Calculator.modulo(numero_1, numero_2)
                                
                            elif opcao == 6:
                                break
                            else:
                                raise ValueError()                        

                        except:
                            print('Informe uma opcao valida!')
                else:
                    print('Informe numeros positivos!')
            except KeyboardInterrupt:
                quit()
            except:
                print('Informe numeros validos!')

if __name__ == '__main__':
    Calculator.controle_operacoes()