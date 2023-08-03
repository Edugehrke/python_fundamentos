# Exercicio 4:
	#Desenvolva uma função que mostre na tela uma contagem regressiva de 5 a 1, com uma pausa de um segundo entre cada número.


import os
import time

def cont_reg():
   
    for i in range(5,0,-1):
        time.sleep(1)
        print(i)

def cont_reg_manual():
    cont = 5
    while True:
        print(cont)
        cont -=  1
        if cont == 0:
            break

if __name__ == '__main__':
    os.system('cls')
    cont_reg()