# Exercicio 5:
	#Crie uma função que exiba uma mensagem perguntando a idade do usuário e, com base na idade fornecida,
	#exiba diferentes mensagens de acordo com as seguintes faixas etárias: 0-12 anos, 13-17 anos, 18 ou mais anos.
	#(mais faixas etárias podem ser incluídas)
import os

def idade():
    while True:
        try:
            idade_valor = int(input('Informe sua idade:'))
            if(idade_valor > 0 and idade_valor <150):
                if idade_valor > 0 and idade_valor <= 12 :
                    print('Voce eh crianca')
                elif idade_valor <18:
                    print('Voce eh jovemmmm')
                else:   
                    print('Voce eh adulto')
                break
            else:
                print('idade invalida!')
        except:
            print('Informe uma idade valida!')
    

if __name__ == '__main__':
    os.system('cls')
    idade()