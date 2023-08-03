

import os

def recebe_data():
    while True:
        try:
            dia = int(input('Informe o dia: '))                       
            if dia > 0 and dia <= 31:
                mes = int(input('Informe o mes: '))
                if mes > 0 and mes <= 12:
                    ano = int(input('Informe o ano: '))
                    if ano >= 1950 and ano <= 2023:
                        return dia, mes, ano
                    else:
                        print('Ano invalido!')
                else:
                    print('Mes invalido!')
            else:
                print('Dia invalido!')




        except:
            print('Informe datas validas!!')

def mostrar_data(dia, mes, ano):
    print(f'a data informada foi {dia}/{mes}/{ano}')

def main():
    dia, mes, ano = recebe_data()
    mostrar_data(dia,mes,ano)

    
if __name__ == '__main__':
    os.system('cls') 
    main()