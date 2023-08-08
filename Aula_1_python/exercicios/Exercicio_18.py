import os 

def informe_quantidade():
    while True:
        try:
            quant = int(input('informe a quantidade de notas que voce deseja: '))
            if quant > 0:          
                return quant
            else:
                raise ValueError('Informe numeros acima de 0')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')
            print('Informe uma quantidade valida!')

def informe_notas(quant_notas):
    lista = []

    while len(lista) < quant_notas:
        try:
            nota = float(input(f'Informe sua nota {len(lista) + 1}º: '))

            if nota >= 0 and nota <= 10:
                lista.append(nota)
            
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')
            print('Informe uma nota valida!')

    return lista

def calc_media(lista):
    soma = 0
    cont = 0
    for item in lista:
        print(f'a sua {cont + 1}ª nota é: {item}')
        soma += item
        cont = cont + 1
    media_final = soma/len(lista)
    print('Portanto, a sua média final é:', media_final)

def main():
    quant_notas = informe_quantidade() 
    lista = informe_notas(quant_notas)
    calc_media(lista)
    



if __name__ == '__main__':
    os.system('cls') 
    main()