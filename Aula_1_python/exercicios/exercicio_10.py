import os 


def ler_dados():
    while True:
        try:
            horas = int(input('Informe o valor em horas para ser convertido: '))
            return horas
        except:
            print('Dados invalidos!')

def converter_dados(horas):
    minutos = round(horas * 60,2)
    segundos = round(horas * 3600,2)
    return minutos, segundos

def exibir_dados(horas, minutos, segundos):
    print(f'A hora {horas} convertida em minutos é: {minutos} min')
    print(f'A hora {horas} convertida em minutos é: {segundos} s')

def main():
    horas = ler_dados()
    minutos, segundos = converter_dados(horas)
    exibir_dados(horas, minutos, segundos)


if __name__ == '__main__':
    os.system('cls') 
    main()
    