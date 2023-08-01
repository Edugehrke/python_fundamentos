import os 

def mostrar_lista():
    lista_dados = [
        1,
        2,
        3,
        'Hello',
        'Hi',
        False,
        True,
        1.5,
        20,
        'Texto !!'
    ]

    for item in lista_dados:
        print(item)

def obter_mostrar_dados():
    lista_input = []

    for i in range(5):
        item = input(f'Informe o {i + 1} Item: ')
        lista_input.append(item)
    
    for item in lista_input:
        print(item)

def script_lista():
    lista_dados = []
    contador = 0

    #Receber 10 itens do usuario
    while contador < 10:
        contador += 1
        item_informado = input(f'Informe o {contador} item: ')
        lista_dados.append(item_informado)
    

    

    #Mostrar os itens recebidos
    for indice, item in enumerate(lista_dados): 
        print(f'Posicao {indice} - Valor {item}')

    

    #Loop para o usuario acessar itens especificos da lista

    while True:
        try:
            posicao_item = int(input('informe a posicao do item desejado: '))
            print(f'O item que esta na posicao {posicao_item} é {lista_dados[posicao_item]}')

            verificacao = input('Informe s para parar, informe outro valor para continuar: ')
            if verificacao == 's':
                break


        except:
            print('Informe apenas inteiros para posicoes em listas!!')

if __name__ == '__main__':
    os.system('cls')
    #mostrar_lista()
    #obter_mostrar_dados()
    script_lista()


