import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from binance_data import get_data



from pyti.simple_moving_average import simple_moving_average as sma
from pyti.exponential_moving_average import exponential_moving_average as ema
from pyti.moving_average_convergence_divergence import moving_average_convergence_divergence as macd
from pyti.stochastic import percent_k, percent_d
from pyti.on_balance_volume import on_balance_volume as obv

def sma_strategy(df):
    signals = []
    
    
    
    df['SMA_7'] = sma(df['Close'], 7)
    df['SMA_29'] = sma(df['Close'], 29)
    
    for i in range(1, len(df)):
        if(df['SMA_7'][i] >= df['SMA_29'][i] and df['SMA_7'][i-1] <= df['SMA_29'][i-1]):
          signals.append([df['Unix'][i],df['Date'][i],df['Close'][i], 0])
        
        else:
            None
            
    for i in range(1, len(df)):    
        if(df['SMA_7'][i] <= df['SMA_29'][i] and df['SMA_7'][i-1] >= df['SMA_29'][i-1]):
           signals.append([df['Unix'][i],df['Date'][i],df['Close'][i], 1])
        
        else:
            None
    
    signals.sort()
    
    for row in signals:
        del row[0]
    
    for i in range(1, len(signals)):
        
        if signals[i][2] == signals[i-1][2]:
           signals.remove(signals[i-1])
        
        elif len(signals) == 0:
             None
        
        else:
            None
    
    if signals[0][2] == 0:
        signals.remove(signals[0])
    else:
        None

    return df, signals


#Effectiveness
def eff(df):
    df, signals = sma_strategy(df)
    signals = pd.DataFrame(signals)
    ef = []
    for i in range(1, len(signals), 2):
        if((signals[1][i] - signals[1][i-1]) > 0):
             ef.append(signals[1][i] - signals[1][i-1])
        else:
            None
        
    effectiveness = len(ef)/(len(signals)/2)  

    return print("Effectivnes is : ", effectiveness)



#Visualization
def visualization(df):
    df, signals = sma_strategy(df)
    signals = pd.DataFrame(signals)
    plt.figure(figsize=(13, 9))

    plt.plot(df['Date'], df['Close'],linewidth=0.5,color='black')
    plt.plot(df['Date'], df['SMA_7'],linewidth=0.5,color='green')
    plt.plot(df['Date'], df['SMA_29'],linewidth=0.5,color='red')


    plt.scatter(signals.loc[signals[2] == 1 , 0].values,signals.loc[signals[2] == 1, 1].values, label='skitscat', color='green', s=25, marker="^")
    plt.scatter(signals.loc[signals[2] == 0 , 0].values,signals.loc[signals[2] ==0, 1].values, label='skitscat', color='red', s=25, marker="^")
   
    return plt.show()
