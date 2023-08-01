import os 
from operador import verifica_idade
from operador import verifica_numeros

def script_idade():
    while True:
        verifica_idade()
        
        verificacao = input('Informe s para sair, e qualquer outro char para continuar: ')
        #Deixar letras minusculas 
        verificacao = verificacao.lower()

        if verificacao == 's':      
            print('Programa parou! ')
            break

def script_numeros(limite_loop):
    
    contador = 0
    while contador < limite_loop:
        contador += 1
        verifica_numeros()
    print(f'O loop rodou {limite_loop} vezes!')

if __name__ == '__main__':
    os.system('cls')
    limite_loop = int(input('Informe quantas vezes o programa deve rodar: '))
    script_numeros(limite_loop)
