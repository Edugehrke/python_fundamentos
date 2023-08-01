import os

def verifica_numeros():

    try:
        primeiro_numero = int(input('Informe um numero: '))
        segundo_numero = int(input('Informe outro numero: '))


        if primeiro_numero > 0 and segundo_numero > 0:
            if primeiro_numero != segundo_numero:
                if primeiro_numero> segundo_numero:
                    print('Primeiro numero é maior que primeiro numero ')
            
                elif primeiro_numero < segundo_numero:
                    print('Primeiro numero é menor que segundo numero')

            elif  primeiro_numero == segundo_numero:
                print('Os dois numeros sao iguais ')
        else:
            print('Numeros precisam ser positivos')




    except:
        print('Erro ao converter os dados para int! ')

def verifica_idade(): 
    try: 
        idade_usuario = int(input('Informe sua idade: '))

        if idade_usuario > 0 and idade_usuario < 120:
            if idade_usuario >= 18:
                print('Voce é um adulto!')
            elif idade_usuario >= 12 and idade_usuario < 18:
                print('Voce é um teen')
            elif idade_usuario < 12:
                print('Voce é uma crianca!')
        else: 
            print('idade invalida! ')


    except:
        print('Erro ao ler dados')



if __name__ == '__main__':
    os.system('cls')
    os.system('python --version')
    verifica_idade()



