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

    command1 = 'tradeTransaction'

    arg1= {
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
    arg2= {
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

#


    command = 'getChartLastRequest'
    command1 = 'tradeTransaction'
    arg1= {
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
    arg2= {
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
            "period": 15,
            "start": delay_time(days=1),
            "symbol": "BITCOIN"
        }
    
    }

    
    minute_price_arg = {

     "info": {
            "period": 1,
            "start": delay_time(days=1),
            "symbol": "BITCOIN"
        }
    
    }


    _15_minutes = 15*60

    stoper = 0

    


    while(1):
        client = APIClient()
        loginResponse = client.execute(loginCommand(userId=userId, password=password))
        logger.info(str(loginResponse)) 

        if(loginResponse['status'] == False):
            print('Login failed. Error code: {0}'.format(loginResponse['errorCode']))
            return

        if stoper == 0:

            json_response = client.commandExecute(command,arg)

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

        minute_price_json_response = client.commandExecute(command,minute_price_arg)
        minute_data = pd.DataFrame(minute_price_json_response['returnData']['rateInfos'])

        minute_data['close'] = minute_data['close'].add(minute_data['open'])
        minute_data['high'] = minute_data['high'].add(minute_data['open'])
        minute_data['low'] = minute_data['low'].add(minute_data['open'])

            
        minute_data['close'] = minute_data['close'].div(100)
        minute_data['high'] = minute_data['high'].div(100)
        minute_data['low'] = minute_data['low'].div(100)

        minute_data.to_csv('data/output.csv', index=False)

        print(minute_data['close'][1425])

        # print(minute_data['close'])

        if minute_data['close'][1425] <= bollinger_down[96]:
            client.commandExecute(command1,arg1)
            print('KUPILEM')
        if minute_data['close'][1425] >= bollinger_up[96]:
            client.commandExecute(command1,arg2)
            print('SPRZEDALEM')




        if step_mode == True:
            break

        client.disconnect()
        time.sleep(1)

        stoper = stoper + 1

        if stoper == _15_minutes:
             stoper = 0

    plt.plot(data['ctm'],data['close'],data['ctm'],bollinger_down,data['ctm'],bollinger_up)
    plt.show()


    

if __name__ == "__main__":
        main()	