# Exercicio 6:
# Crie uma função que solicite ao usuário que insira seu endereço completo (incluindo rua, número, bairro, cidade e CEP) e 
# armazene as informações em variáveis separadas. Depois mostre essas informações usando concatenação com uma mensagem.

import os


def receba_dados_endereco() :
    while True:
        try:
            rua= str(input('Informe sua rua: '))
            nmr= int(input('Informe seu numero: '))
            bairro= int(input('Informe seu bairro: '))
            cidade= str(input('Informe sua cidade: '))
            cep= int(input('Informe seu CEP: '))
            break
        except:
            print('Dados invalidos!')

    return rua, nmr, bairro, cidade, cep

def mostra_dados_endereco(rua, nmr, bairro, cidade, cep):
    print(f'Rua: {rua} {nmr} Bairro: {bairro} cidade: {cidade} e o CEP: {cep}')


if __name__ == '__main__':
    os.system('cls')
    rua, nmr, bairro, cidade, cep = receba_dados_endereco()
    mostra_dados_endereco(rua, nmr, bairro, cidade, cep)