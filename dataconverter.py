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

client = APIClient()
userId = os.getenv('USER_ID')
password = os.getenv('USER_PASSWORD')
def closingprices1(data):
    load_dotenv()
    data['close'] = data['close'].add(data['open'])
    data['close'] = data['close'].div(100)
    data.index = np.arange(data.shape[0])
    closing_prices = data['close']
    return closing_prices