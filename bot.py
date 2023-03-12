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

    client = APIClient()
    
    loginResponse = client.execute(loginCommand(userId=userId, password=password))
    logger.info(str(loginResponse)) 

    if(loginResponse['status'] == False):
        print('Login failed. Error code: {0}'.format(loginResponse['errorCode']))
        return
    

    command = 'getChartLastRequest'


    arg = {

     "info": {
            "period": 1440,
            "start": delay_time(days=200),
            "symbol": "AAPL.US_9"
        }
    
    }

    while(1):

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

        if data['close'][19]==bollinger_down[19]:
             buy = 1
        else:
             buy = 0

        print(buy)
        if step_mode == True:
            break
        time.sleep(1)

    plt.plot(data['ctm'],data['close'],data['ctm'],bollinger_down,data['ctm'],bollinger_up)
    plt.show()


    client.disconnect()

if __name__ == "__main__":
        main()	