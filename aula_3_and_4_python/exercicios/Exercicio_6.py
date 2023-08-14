 #       6 - Classe Aluno:
 #       Crie uma classe chamada Aluno que represente um aluno. A classe deve ter os atributos nome, matricula e notas (uma lista de notas).
  #      Crie métodos para calcular a média (calcular_media()) e exibir o status do aluno com base na média (exibir_status()).
import os

class Aluno:
    
    nome = 'Edu'
    matricula = 2131231
    lista_notas = [10,5,7]


    def calcular_media():
        while True:
            try:
                os.system('cls')
                soma = 0
                cont = 0
                for item in Aluno.lista_notas:
                    print(f'A {cont + 1}ª do aluno {Aluno.nome}, {Aluno.matricula} é: {item}')                          
                    soma = soma + item
                    cont = cont + 1
                media = soma/len(Aluno.lista_notas)
                print('A Media do aluno  é: ', media)
                
                if media < 6:
                    print('O aluno reprovou!')
                    break
                else:
                    print('Aluno aprovado!')
                break
            except: 
                print('Nao foi possivel, tente novamente!')
Aluno.calcular_media()