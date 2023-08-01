import os

def captura_dados():
        # Lendo dados do usuario 
    texto_usuario = input('Informe um texto: ')
    print('Voce escreveu => ', texto_usuario)    
    print(type(texto_usuario))
    
    inteiro_usuario = input('Informe um numero: ')
    # Try -> para tentar executar o codigo e continuar caso haja erro
    try:  
        inteiro_usuario = int(inteiro_usuario)
    except:
        print('Erro ao tentar converter inteiro! ')
    
    print(type(inteiro_usuario))
    print('Voce escreveu => ', inteiro_usuario)

    float_usuario = input('Informe um numero float: ')
    try:
        float_usuario = float(float_usuario)
    except:
        print('Erro ao tentar converter float! ')
    
    print('Voce escreveu => ', float_usuario)
    print(type(float_usuario))

if __name__ == '__main__':
    os.system('cls')
    print('Executando primeira vez: ')
    captura_dados()
    print('Executando segunda vez: ')
    captura_dados()
    print('Executando terceira vez: ')
    captura_dados()
