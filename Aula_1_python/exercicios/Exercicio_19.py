# Escrever uma função que solicita ao usuário uma senha e verifica se ela atende a alguns critérios de segurança.
# Usar laço de repetição para rodar até uma senha válida ser informada e a mesma ser informada duas vezes de
# forma identica para confirmação da senha.
# Critérios de segurança:
# A senha deve conter pelo menos 8 caracteres.
# A senha deve conter pelo menos uma letra maiúscula e uma letra minúscula.
# A senha deve conter pelo menos um número.

import os


def receber_senha_valida(): 
    lista_letras_minusculas = [
        'a', 'b', 'c', 'd', 'e', 'f'
        'g', 'h', 'i', 'j' 'k', 'l', 'm'
        'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]

    lista_letras_maiusculas = [
        'A', 'B', 'C', 'D', 'E', 'F'
        'G', 'H', 'I', 'J' 'K', 'L', 'M'
        'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    senha = ''
    validou = False
    while validou is False:
        senha = input('Informe sua senha: ')
        if len(senha) < 8:
            print('Senha nao tem 8 chars')                
        else:
            senha_list = list(senha)

            achou_mai = False
            achou_min = False
            for letra in senha_list:
                if letra in lista_letras_maiusculas:
                    achou_mai = True

                if letra in lista_letras_minusculas:
                    achou_min = True

            achou_numero = False
            if achou_min is True and achou_mai is True:
                for char in senha_list:
                    if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        achou_numero = True
                        break
                
                if achou_numero is True:
                    senha_nova = input('Informe a senha novamente: ')
                    if senha_nova == senha:
                        print('Criou senha com sucesso')
                        validou = True
                    else:
                        print('Senhas nao batem')
                else:
                    print('Nao achou nuemro na senha')
            else:
                print('Nao achou maiusculas e minusculas na mesma senha')

                    



            
            

 

        
        




if __name__ == '__main__':
    os.system('cls')    
    receber_senha_valida()
