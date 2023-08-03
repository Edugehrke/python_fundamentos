# Exercicio 2:
	#Escreva uma função que calcule a média de três notas fornecidas pelo usuário e
	#armazene o resultado em uma variável. Em seguida, exiba a média calculada no terminal.

import os


def calcula_media():
    media = 0
    try: 
        for i in range(3):
             valor = int(input(f'Insira o {i + 1} valor para media: '))
             media = valor + media
        media = media/3
        print('A sua media é: ', media)
    except:
        print('Nao é um valor valido!')
       
if __name__ == '__main__':
    os.system('cls')
    calcula_media()

        
        
        