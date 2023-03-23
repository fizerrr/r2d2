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
from tradeshistory import  getallsymbols
from RSI import calculate_rsi
from dataconverter import closingprices1
# Debug mode
debug_mode = False
arguments=1
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
    if arguments ==1:
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
        arg_apple ={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "BINANCECOIN"
            }
        }
        arg_microsoft={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "AAPL.US_9"
            }
        }
        arg_alior={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "ALR.PL_9"
            }
        }
        arg_allegro={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "ALE.PL_9"
            }
        }
        arg_asseco={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "ACP.PL_9"
            }
        }
        arg_cdprojekt={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "CDR.PL_9"
            }
        }
        arg_cyfrplst={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "CPS.PL_9"
            }
        }
        arg_dino={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "DNP.PL_9"
            }
        }
        arg_JSW={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "JSW.PL_9"
            }
        }
        arg_KETY={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "KTY.PL_9"
            }
        }
        arg_kghm={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "KGH.PL_9"
            }
        }
        arg_KRUK={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "KRU.PL_9"
            }
        }
        arg_LPP={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "LPP.PL_9"
            }
        }

        arg_MBANK={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "MBK.PL_9"
            }
        }
        arg_Orange={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "ORA.FR_9"
            }
        }
    
        arg_Pekao={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "PEO.PL_9"
            }
        }
        arg_Pepco={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "PCO.PL"
            }
        }
        arg_Pge={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "PGE.PL_9"
            }
        }
        arg_Orlen={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "PKN.PL_9"
            }
        }
        arg_Pkobp={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "PKO.PL_9"
            }
        }
        arg_Pzu={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "PZU.PL_9"
            }
        }
        arg_Sanpl={

            "info": {
                "period": 1440,
                "start": delay_time(days=50),
                "symbol": "SPL.PL_9"
            }
        }
        


        arg_tradeshistory ={
            "end": 0,
            "start": 1678045116000
        }
        
        minute_price_arg = {

            "level": 0,
            "symbols": [
                "BITCOIN",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_apple = {

            "level": 0,
            "symbols": [
                "BINANCECOIN",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_alior = {

            "level": 0,
            "symbols": [
                "ALR.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_allegro = {

            "level": 0,
            "symbols": [
                "ALE.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_asseco = {

            "level": 0,
            "symbols": [
                "ACP.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_cdprojekt = {

            "level": 0,
            "symbols": [
                "CDR.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_cyfrplst = {

            "level": 0,
            "symbols": [
                "CPS.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_dino = {

            "level": 0,
            "symbols": [
                "DNP.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_JSW= {

            "level": 0,
            "symbols": [
                "JSW.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
    
        minute_price_arg_KETY = {

            "level": 0,
            "symbols": [
                "KTY.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
    
        minute_price_arg_kghm = {

            "level": 0,
            "symbols": [
                "KGH.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
    
        minute_price_arg_KRUK = {

            "level": 0,
            "symbols": [
                "KRU.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
    
        minute_price_arg_LPP = {

            "level": 0,
            "symbols": [
                "LPP.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
    
        minute_price_arg_MBANK= {

            "level": 0,
            "symbols": [
                "MBK.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
    
        minute_price_arg_Orange = {

            "level": 0,
            "symbols": [
                "ORA.FR_9",
            ],
            "timestamp": delay_time(days=0)
        }
    
        minute_price_arg_PEKAO= {

            "level": 0,
            "symbols": [
                "PEO.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_Pepco= {

            "level": 0,
            "symbols": [
                "PCO.PL",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_Pge= {

            "level": 0,
            "symbols": [
                "PGE.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        minute_price_arg_Orlen= {

            "level": 0,
            "symbols": [
                "PKN.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        
        minute_price_arg_Pzu = {

            "level": 0,
            "symbols": [
                "PZU.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        
        minute_price_arg_Sanpl= {

            "level": 0,
            "symbols": [
                "SPL.PL_9",
            ],
            "timestamp": delay_time(days=0)
        }
        
        minute_price_arg_Pkobp= {

            "level": 0,
            "symbols": [
                "PKO.PL_9",
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
    json_symbols = client.commandExecute('getAllSymbols')
    getallsymbols( json_symbols)
    if(loginResponse['status'] == False):
        print('Login failed. Error code: {0}'.format(loginResponse['errorCode']))
        return
    


    while(1):


        if stoper == 0:

            json_response = client.commandExecute(command_getChartLastRequest,arg)
            json_response_apple = client.commandExecute(command_getChartLastRequest,arg_apple)
            json_response_alior = client.commandExecute(command_getChartLastRequest,arg_alior)
            json_response_allegro = client.commandExecute(command_getChartLastRequest,arg_allegro)
            json_response_asseco = client.commandExecute(command_getChartLastRequest,arg_asseco)
            json_response_cdprojekt = client.commandExecute(command_getChartLastRequest,arg_cdprojekt)
            json_response_cyfplst = client.commandExecute(command_getChartLastRequest,arg_cyfrplst)
            json_response_dino = client.commandExecute(command_getChartLastRequest,arg_dino)
            json_response_JSW = client.commandExecute(command_getChartLastRequest,arg_JSW)
            json_response_KETY = client.commandExecute(command_getChartLastRequest,arg_KETY)
            json_response_kghm = client.commandExecute(command_getChartLastRequest,arg_kghm)
            json_response_KRUK = client.commandExecute(command_getChartLastRequest,arg_KRUK)
            json_response_MBANK = client.commandExecute(command_getChartLastRequest,arg_MBANK)
            json_response_Orange = client.commandExecute(command_getChartLastRequest,arg_Orange)
            json_response_LPP = client.commandExecute(command_getChartLastRequest,arg_LPP)
            json_response_Pekao = client.commandExecute(command_getChartLastRequest,arg_Pekao)
            json_response_Pepco = client.commandExecute(command_getChartLastRequest,arg_Pepco)
            json_response_Pge = client.commandExecute(command_getChartLastRequest,arg_Pge)
            json_response_Orlen = client.commandExecute(command_getChartLastRequest,arg_Orlen)
            json_response_Pkobp = client.commandExecute(command_getChartLastRequest,arg_Pkobp)
            json_response_Pzu = client.commandExecute(command_getChartLastRequest,arg_Pzu)
            json_response_Sanpl = client.commandExecute(command_getChartLastRequest,arg_Sanpl)



            #if debug_mode == True:
                #with open("data/response.json", "w") as f:
                #    json.dump(json_response, f)
                #with open("data_apple/response.json", "w") as f:
                   # json.dump(json_response, f)

            data = pd.DataFrame(json_response['returnData']['rateInfos'])
            data_apple = pd.DataFrame(json_response_apple['returnData']['rateInfos'])
            data_alior = pd.DataFrame(json_response_alior['returnData']['rateInfos'])
            data_allegro = pd.DataFrame(json_response_allegro['returnData']['rateInfos'])
            data_asseco = pd.DataFrame(json_response_asseco['returnData']['rateInfos'])
            data_cdprojekt = pd.DataFrame(json_response_cdprojekt['returnData']['rateInfos'])
            data_cyfplst = pd.DataFrame(json_response_cyfplst['returnData']['rateInfos'])
            data_dino = pd.DataFrame(json_response_dino['returnData']['rateInfos'])
            data_JSW = pd.DataFrame(json_response_JSW['returnData']['rateInfos'])
            data_KETY = pd.DataFrame(json_response_KETY['returnData']['rateInfos'])
            data_kghm = pd.DataFrame(json_response_kghm['returnData']['rateInfos'])
            data_KRUK = pd.DataFrame(json_response_KRUK['returnData']['rateInfos'])
            data_MBANK = pd.DataFrame(json_response_MBANK['returnData']['rateInfos'])
            data_Orange = pd.DataFrame(json_response_Orange['returnData']['rateInfos'])
            data_LPP = pd.DataFrame(json_response_LPP['returnData']['rateInfos'])
            data_Pekao = pd.DataFrame(json_response_Pekao['returnData']['rateInfos'])
            data_Pepco = pd.DataFrame(json_response_Pepco['returnData']['rateInfos'])
            data_Pge = pd.DataFrame(json_response_Pge['returnData']['rateInfos'])
            data_Orlen = pd.DataFrame(json_response_Orlen['returnData']['rateInfos'])
            data_Pkobp = pd.DataFrame(json_response_Pkobp['returnData']['rateInfos'])
            data_Pzu = pd.DataFrame(json_response_Pzu['returnData']['rateInfos'])
            data_Sanpl = pd.DataFrame(json_response_Sanpl['returnData']['rateInfos'])

            closing_prices=closingprices1(data)
            closing_prices_alior= closingprices1(data_alior)
            closing_prices_allegro = closingprices1(data_allegro)
            closing_prices_asseco = closingprices1(data_asseco)
            closing_prices_cdprojekt = closingprices1(data_cdprojekt)
            closing_prices_cyfplst = closingprices1(data_cyfplst)
            closing_prices_dino = closingprices1(data_dino)
            closing_prices_JSW= closingprices1(data_JSW)
            closing_prices_KETY = closingprices1(data_KETY)
            closing_prices_kghm  = closingprices1(data_kghm)
            closing_prices_KRUK = closingprices1(data_KRUK)
            closing_prices_MBANK = closingprices1(data_MBANK)
            closing_prices_Orange = closingprices1(data_Orange)
            closing_prices_LPP = closingprices1(data_LPP)
            closing_prices_Pekao = closingprices1(data_Pekao)
            closing_prices_Pepco = closingprices1(data_Pepco)
            closing_prices_Pge = closingprices1(data_Pge)
            closing_prices_Orlen = closingprices1(data_Orlen)
            closing_prices_Pkobp = closingprices1(data_Pkobp)
            closing_prices_Pzu = closingprices1(data_Pzu)
            closing_prices_Sanpl = closingprices1(data_Sanpl)
        
            #data['close'] = data['close'].add(data['open'])
            #data['high'] = data['high'].add(data['open'])
           # data['low'] = data['low'].add(data['open'])
            #data['close'] = data['close'].div(100)
            #data['high'] = data['high'].div(100)
            #data['low'] = data['low'].div(100)
            #if debug_mode == True:
               # data.to_csv('data/output.csv', index=False)
            

         
            
            
        #96

        minute_price_json_response = client.commandExecute('getTickPrices',minute_price_arg)
        minute_price_json_response_alior = client.commandExecute('getTickPrices',minute_price_arg_alior )
        minute_price_json_response_allegro = client.commandExecute('getTickPrices',minute_price_arg_allegro )
        minute_price_json_response_asseco = client.commandExecute('getTickPrices',minute_price_arg_asseco )
        minute_price_json_response_cdprojekt = client.commandExecute('getTickPrices',minute_price_arg_cdprojekt )
        minute_price_json_response_cyfrplst = client.commandExecute('getTickPrices',minute_price_arg_cyfrplst )
        minute_price_json_response_dino = client.commandExecute('getTickPrices',minute_price_arg_dino )
        minute_price_json_response_JSW = client.commandExecute('getTickPrices',minute_price_arg_JSW )
        minute_price_json_response_KETY = client.commandExecute('getTickPrices',minute_price_arg_KETY )
        minute_price_json_response_kghm = client.commandExecute('getTickPrices',minute_price_arg_kghm )
        minute_price_json_response_KRUK = client.commandExecute('getTickPrices',minute_price_arg_KRUK )
        minute_price_json_response_MBANK = client.commandExecute('getTickPrices',minute_price_arg_MBANK )
        minute_price_json_response_Orange = client.commandExecute('getTickPrices',minute_price_arg_Orange )
        minute_price_json_response_LPP = client.commandExecute('getTickPrices',minute_price_arg_LPP )
        minute_price_json_response_PEKAO = client.commandExecute('getTickPrices',minute_price_arg_PEKAO )
        minute_price_json_response_Pepco = client.commandExecute('getTickPrices',minute_price_arg_Pepco )
        minute_price_json_response_Pge = client.commandExecute('getTickPrices',minute_price_arg_Pge )
        minute_price_json_response_Orlen = client.commandExecute('getTickPrices',minute_price_arg_Orlen )
        minute_price_json_response_Pkobp = client.commandExecute('getTickPrices',minute_price_arg_Pkobp )
        minute_price_json_response_Pzu = client.commandExecute('getTickPrices',minute_price_arg_Pzu )
        minute_price_json_response_Sanpl = client.commandExecute('getTickPrices',minute_price_arg_Sanpl )
        # minute_data['close'] = minute_data['close'].add(minute_data['open'])
        # minute_data['high'] = minute_data['high'].add(minute_data['open'])
        # minute_data['low'] = minute_data['low'].add(minute_data['open'])
        # minute_data['close'] = minute_data['close'].div(100)
        # minute_data['high'] = minute_data['high'].div(100)
        # minute_data['low'] = minute_data['low'].div(100)
        # minute_data.to_csv('data/output.csv', index=False)
        
        data_price = pd.DataFrame(minute_price_json_response['returnData']['quotations'])
        data_price_alior = pd.DataFrame(minute_price_json_response_alior['returnData']['quotations'])
        data_price_allegro = pd.DataFrame(minute_price_json_response_allegro['returnData']['quotations'])
        data_price_asseco = pd.DataFrame(minute_price_json_response_asseco['returnData']['quotations'])
        data_price_cdprojekt = pd.DataFrame(minute_price_json_response_cdprojekt['returnData']['quotations'])
        data_price_cyfplst = pd.DataFrame(minute_price_json_response_cyfrplst['returnData']['quotations'])
        data_price_dino = pd.DataFrame(minute_price_json_response_dino['returnData']['quotations'])
        data_price_JSW = pd.DataFrame(minute_price_json_response_JSW['returnData']['quotations'])
        data_price_kghm = pd.DataFrame(minute_price_json_response_KETY['returnData']['quotations'])
        data_price_KRUK = pd.DataFrame(minute_price_json_response_kghm['returnData']['quotations'])
        data_price_MBANK = pd.DataFrame(minute_price_json_response_KRUK['returnData']['quotations'])
        data_price_Orange = pd.DataFrame(minute_price_json_response_LPP['returnData']['quotations'])
        data_price_LPP = pd.DataFrame(minute_price_json_response_Pkobp['returnData']['quotations'])
        data_price_Pekao = pd.DataFrame(minute_price_json_response_Sanpl['returnData']['quotations'])
        data_price_Pepco = pd.DataFrame(minute_price_json_response_Pzu['returnData']['quotations'])
        data_price_Pge = pd.DataFrame(minute_price_json_response_MBANK['returnData']['quotations'])
        data_price_Orlen = pd.DataFrame(minute_price_json_response_Orange['returnData']['quotations'])
        data_price_Pkobp = pd.DataFrame(minute_price_json_response_Orlen['returnData']['quotations'])
        data_price_Pzu = pd.DataFrame(minute_price_json_response_PEKAO['returnData']['quotations'])
        data_price_Sanpl = pd.DataFrame(minute_price_json_response_Pepco['returnData']['quotations'])
        data_price_Sanpl = pd.DataFrame(minute_price_json_response_Pge['returnData']['quotations'])
        
        bollinger_up, bollinger_down = get_bollinger_bands(closing_prices)
        rsi_ratio=calculate_rsi(closing_prices)
        
        print("//////RSI_ratio//////\n")
        print(rsi_ratio)  
        print("/////////////////////\n")   
        print("//////RSI_ratio//////\n")
        print("/////////////////////\n") 
            
        
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