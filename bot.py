from dotenv import load_dotenv
from xAPIConnector import APIClient,loginCommand,logger
import os
import numpy as np
import json,pandas as pd
from bollinger_bands import get_bollinger_bands
from functions_time import delay_time
import matplotlib.pyplot as plt
import time

# Debug mode
debug_mode = False

# True = off loop
step_mode = False

def main():
        
    load_dotenv()


    userId = os.getenv('USER_ID')
    password = os.getenv('USER_PASSWORD')

  
    
    # loginResponse = client.execute(loginCommand(userId=userId, password=password))
    # logger.info(str(loginResponse)) 

    # if(loginResponse['status'] == False):
    #     print('Login failed. Error code: {0}'.format(loginResponse['errorCode']))
    #     return
    

# wirus

    command_tradeTransaction = 'tradeTransaction'

    command_getChartLastRequest = 'getChartLastRequest'
    symbol = "ALGORAND"

    arg_buy= {
        "tradeTransInfo": {
            "cmd": 0,
            "customComment": "Some text",
            "expiration": 0,
            "order": 0,
            "price": 1.4,
            "sl": 0,
            "tp": 0,
            "symbol": symbol,
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
            "symbol": symbol,
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
            "symbol": symbol,
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
            "symbol": symbol,
            "type": 0,
            "volume": 0.05
        }
    }

    arg = {

     "info": {
            "period": 1440,
            "start": delay_time(days=50),
            "symbol": symbol
        }
    
    }

    
    minute_price_arg = {

        "level": 0,
        "symbols": [
            symbol,
        ],
        "timestamp": delay_time(days=0)
    }


    _15_minutes = 15*60

    stoper = 0
    client = APIClient()
    loginResponse = client.execute(loginCommand(userId=userId, password=password))
    logger.info(str(loginResponse)) 

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
        print('BOLLINGER:')
        print(bollinger_down[50],bollinger_up[50])



        if data_price['ask'][0] <= bollinger_down[50]:
            client.commandExecute(command_tradeTransaction,arg_buy)
            print('KUPILEM')
        if data_price['ask'][0] >= bollinger_up[50]:
            client.commandExecute(command_tradeTransaction,arg_sell)
            print('SPRZEDALEM')


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