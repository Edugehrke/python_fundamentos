import pandas as pd
import os 


def dolar_atual():
    url = 'https://www.bcb.gov.br/pec/deflator/'
    df = pd.read_csv(url, parse_dates=True, index_col='data')
    dollar_value = df['USD']['venda'].iloc[-1]
    print(dollar_value)

if __name__ == '__main__':
    os.system('cls') 
    dolar_atual()


# a fazer