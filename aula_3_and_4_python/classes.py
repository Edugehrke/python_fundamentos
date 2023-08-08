

class ClasseCachorro:
     # Atributos
    idade = 5
    raca = 'Pastor Alemao'

    def latir(latidas):
        for latida in range(latidas):
            print('au au')


    def comer(comida, horario):
        print(f'au au, comi {comida}, au au em horario {horario}')

    def mostrar_info_dog():
        print(f'O cachorro é da raca {ClasseCachorro.raca}, e tem {ClasseCachorro.idade} anos')



ClasseCachorro.latir(10)
ClasseCachorro.comer('racao','10am')
ClasseCachorro.mostrar_info_dog()



class ClassePessoa:
    # atributos = variaveis
    nome = 'Edu'
    idade = 21 
    altura = 1.72
    peso = 80
    pais_origem = 'Brasil'
    genero = 'Masc'

# métodos - funcoes

    def dizer_ola():
         print(f'Ola, eu sou {ClassePessoa.nome}')

    def mostrar_dados():
         print(f'eu tenho {ClassePessoa.idade} anos, {ClassePessoa.altura} altura, {ClassePessoa.peso} peso e meu genero é {ClassePessoa.genero}')
    
    def mostrar_origem():
        print(f'Eu venho do {ClassePessoa.pais_origem}')


