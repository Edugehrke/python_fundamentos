#Exercicio 7


import os

def le_film_fav():
    lista_filmes = []
    while len(lista_filmes) < 3:
        try:
            filme_informado = str(input(f'Informe o {len(lista_filmes) + 1}º filme: '))
            if len(filme_informado)  > 0:
                lista_filmes.append(filme_informado)
        except Exception as e:
            print(f'Erro: {str(e)}')
    return lista_filmes

def mostra_film_fav(lista_filmes):
    for i, item in enumerate(lista_filmes):
        print(f'{i + 1}º filme: {item}')

def main():
    lista_filmes = le_film_fav()
    mostra_film_fav(lista_filmes)



if __name__ == '__main__':
    os.system('cls')    
    main()