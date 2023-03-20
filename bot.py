from dotenv import load_dotenv
from xAPIConnector import APIClient,loginCommand,logger
import os
import numpy as np
import json,pandas as pd
from bollinger_bands import get_bollinger_bands
from functions_time import delay_time
import matplotlib.pyplot as plt
import time
from tradeshistory import tradeshistory
from RSI import calculate_rsi
# Debug mode
debug_mode = False

# True = off loop
step_mode = False

def main():
        
    load_dotenv()
    
    userId = os.getenv('USER_ID')
    password = os.getenv('USER_PASSWORD')

  
    
   # loginResponse = client.execute(loginCommand(userId=userId, password=password))
    #logger.info(str(loginResponse)) 

    #if(loginResponse['status'] == False):
     #   print('Login failed. Error code: {0}'.format(loginResponse['errorCode']))
      #  return
    

# wirus
    
    command_tradeTransaction = 'tradeTransaction'

    command_getChartLastRequest = 'getChartLastRequest'
    
    command_getTradesHistory = 'getTradesHistory'

    arg_buy= {
        "tradeTransInfo": {
            "cmd": 0,
            "customComment": "Some text",
            "expiration": 0,
            "order": 0,
            "price": 1.4,
            "sl": 0,
            "tp": 0,
            "symbol": "BITCOIN",
            "type": 0,
            "volume": 0.05
        }
    }
    arg_sell= {
        "tradeTransInfo": {
            "cmd": 1,
            "customComment": "Some text",
            "expiration": 0,
            "order": 0,
            "price": 1.4,
            "sl": 0,
            "tp": 0,
            "symbol": "BITCOIN",
            "type": 0,
            "volume": 0.05
        }
    }


    arg_buy= {
        "tradeTransInfo": {
            "cmd": 0,
            "customComment": "Some text",
            "expiration": 0,
            "order": 0,
            "price": 1.4,
            "sl": 0,
            "tp": 0,
            "symbol": "BITCOIN",
            "type": 0,
            "volume": 0.05
        }
    }
    arg_sell= {
        "tradeTransInfo": {
            "cmd": 1,
            "customComment": "Some text",
            "expiration": 0,
            "order": 0,
            "price": 1.4,
            "sl": 0,
            "tp": 0,
            "symbol": "BITCOIN",
            "type": 0,
            "volume": 0.05
        }
    }

    arg = {

     "info": {
            "period": 1440,
            "start": delay_time(days=50),
            "symbol": "BITCOIN"
        }
    
    }

    arg_tradeshistory ={

        
    
   
        "end": 0,
        "start": 1678657600696
    }
    
    minute_price_arg = {

        "level": 0,
        "symbols": [
            "BITCOIN",
        ],
        "timestamp": delay_time(days=0)
    }
    _15_minutes = 15*60
    stoper = 0
    time_enough_to_buy=0
    time_enough_to_sell=0
    client = APIClient()
    loginResponse = client.execute(loginCommand(userId=userId, password=password))
    logger.info(str(loginResponse)) 
    json_trade_history = client.commandExecute(command_getTradesHistory,arg_tradeshistory)
    tradeshistory(json_trade_history)

    if(loginResponse['status'] == False):
        print('Login failed. Error code: {0}'.format(loginResponse['errorCode']))
        return
    


    while(1):


        if stoper == 0:

            json_response = client.commandExecute(command_getChartLastRequest,arg)

            if debug_mode == True:
                with open("data/response.json", "w") as f:
                    json.dump(json_response, f)

            data = pd.DataFrame(json_response['returnData']['rateInfos'])


            data['close'] = data['close'].add(data['open'])
            data['high'] = data['high'].add(data['open'])
            data['low'] = data['low'].add(data['open'])

            
            data['close'] = data['close'].div(100)
            data['high'] = data['high'].div(100)
            data['low'] = data['low'].div(100)

            if debug_mode == True:
                data.to_csv('data/output.csv', index=False)

            data.index = np.arange(data.shape[0])
            closing_prices = data['close']

            bollinger_up, bollinger_down = get_bollinger_bands(closing_prices)
            rsi_ratio=calculate_rsi(closing_prices)
            print("//////RSI_ratio//////\n")
            print(rsi_ratio)  
            print("/////////////////////\n")   
            
            
        #96

        minute_price_json_response = client.commandExecute('getTickPrices',minute_price_arg)
        

        # minute_data['close'] = minute_data['close'].add(minute_data['open'])
        # minute_data['high'] = minute_data['high'].add(minute_data['open'])
        # minute_data['low'] = minute_data['low'].add(minute_data['open'])

            
        # minute_data['close'] = minute_data['close'].div(100)
        # minute_data['high'] = minute_data['high'].div(100)
        # minute_data['low'] = minute_data['low'].div(100)

        # minute_data.to_csv('data/output.csv', index=False)

        
        data_price = pd.DataFrame(minute_price_json_response['returnData']['quotations'])
        print('CENA:')
        print(data_price['ask'][0])
        print('\n')
        print('BOLLINGER:')
        print(bollinger_down[49],bollinger_up[49])
        print('\n')



        if data_price['ask'][0] <= bollinger_down[49] and rsi_ratio<75:
            time_enough_to_buy=time_enough_to_buy+1
        else:
            time_enough_to_buy=0
            
        if time_enough_to_buy==60:
            client.commandExecute(command_tradeTransaction,arg_buy)
            print("KUPIŁEM")
            time_enough_to_buy=0
        if data_price['ask'][0] >= bollinger_up[49]and rsi_ratio>25:
            time_enough_to_sell=time_enough_to_sell+1
        else:
            time_enough_to_sell=0
        if time_enough_to_sell==60:
            client.commandExecute(command_tradeTransaction,arg_sell)
            print('SPRZEDALEM')
            time_enough_to_sell=0


        plt.plot(data['ctm'],data['close'],data['ctm'],bollinger_down,data['ctm'],bollinger_up)
        

        if step_mode == True:
            break

        
        time.sleep(1)

        stoper = stoper + 1

        if stoper == _15_minutes:
             stoper = 0

    client.disconnect()
    plt.plot(data['ctm'],data['close'],data['ctm'],bollinger_down,data['ctm'],bollinger_up)
    plt.show()


    

if __name__ == "__main__":
        main()	