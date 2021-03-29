import pandas as pd
import time

from binance.client import Client
from BINANCE_API import BINANCE_API_KEY, BINANCE_SECRET_KEY



#----------------- Client
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)



#----------------- Get Data
def get_data(pair):
    times = []
    unix = []
    close_price = []
    volume = []
    pair_data = client.get_historical_klines(pair, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    
    for i in range(len(pair_data)):
        times.append(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(pair_data[i][6]/1000)))
        
    for i in range(len(pair_data)):
        unix.append(pair_data[i][6])
        
    for i in range(len(pair_data)):
        close_price.append(pair_data[i][4])
        
    for i in range(len(pair_data)):
        volume.append(pair_data[i][5])
        
    df = pd.DataFrame({'Date':times,
                       'Unix':unix,
                      'Close':close_price,
                      'Volume':volume
                      })
    
    df['Close'] = df['Close'].astype(float)
    df = df.set_index(df['Date'])
    
        
    return df