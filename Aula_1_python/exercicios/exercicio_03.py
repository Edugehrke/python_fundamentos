# Exercicio 3:
	# Crie uma função que peça ao usuário que digite um número inteiro e, em seguida,
	# armazene esse valor em uma variável. Crie mais funções para o usuário também informar 
	# dados do tipo float e string, e armazene todos os dados em variáveis. Em seguida
	# adicione todos esses items em uma lista e mostre os item através de um laço de repetição for. 

import os

def informe_int():
    valor = input('Informe um valor inteiro: ')
    lista.append(valor)

def informe_float():
    valor_float = input('Informe um valor float: ')
    lista.append(valor_float)

def informe_str():
    valor_str = input('Informe um texto: ')
    lista.append(valor_str)

if __name__ == '__main__':
    os.system('cls')

    lista = []

    informe_int()
    informe_float()
    informe_str()

    for i in lista:
        print(i)
    