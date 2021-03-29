import pandas as pd
import time

from binance_data import get_data
from ta_calculator import sma_strategy, eff, visualization



print('Choose traiding pair(e.g. BTCUSDT): ')
pair = input()
#df = get_data(pair)
#df, signals = sma_strategy(df)
#effect = eff(df) #optional
#vizual = visualization(df) #optional
transactions = []

def main(pair):
    df = get_data(pair)
    df, signals = sma_strategy(df)
    
    if signals[-1][2] == 1:
       return signals[-1][0], signals[-1][1], 'BUY'
        
    else:
        return signals[-1][0], signals[-1][1], 'SELL'





if __name__ == "__main__":

    start_time = time.time()
    seconds = 3600

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        last_signal = main(pair)
        if elapsed_time > seconds:
           print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
           break
        
        elif elapsed_time < seconds: 
              if last_signal[2] == 'SELL' and len(transactions) == 0:
                 None 
             
              elif last_signal[2] == 'BUY' or last_signal[2] == 'SELL':
                   if len(transactions) == 0:
                      transactions.append(last_signal) 
                      print(transactions)
             
                   elif len(transactions) != 0:   
                         if transactions[-1][2] == last_signal[2]:
                            None
             
                         elif transactions[-1][2] != last_signal[2]:
                              transactions.append(last_signal)
                              print(transactions)
                        
                         else:
                             print('Error_3')
                
                   else:
                       print('Error_2')
              else:
                  print('Error_1')
             
        
        else:
            print('Error_0')


        