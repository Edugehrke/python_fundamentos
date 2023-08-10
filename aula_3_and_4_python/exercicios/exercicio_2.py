        #2 - Classe Livro:
        #Crie uma classe chamada Livro que represente um livro.
        #A classe deve ter os atributos titulo, autor e ano. Crie um método para exibir as informações do livro (exibir_informacoes()).


class Livro:
    titulo = 'O Garoto do pijama listrado'
    autor = 'George RR Martin'
    ano = 2021
    


    def Exibe_funcoes():
        print(Livro.ano)
        print(Livro.autor)
        print(Livro.titulo)


if __name__ == '__main__':
    Livro.Exibe_funcoes()
