import plotly.graph_objs as go
import xtbapiclient as xapi


API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
API_HOST = 'xapi.xtb.com'
API_PORT = 5124
API_STREAMING_PORT = 5125

api_client = xapi.connect(API_KEY, API_SECRET, API_HOST, API_PORT, API_STREAMING_PORT)

account_info = api_client.get_account_info()
print('Account ID:', account_info.accountId)
print('Balance:', account_info.balance)
print('Equity:', account_info.equity)

order = api_client.create_market_order('EURUSD', 'buy', 0.01)
print('Order ID:', order.orderId)
print('Trade ID:', order.tradeId)
print('Profit/Loss:', order.profit)


order = api_client.create_market_order('EURUSD', 'sell', 0.01)
print('Order ID:', order.orderId)
print('Trade ID:', order.tradeId)
print('Profit/Loss:', order.profit)

symbol = 'AAPL.US'
period = 'D1'
start_date = '2021-01-01'
end_date = '2022-01-01'
data = api_client.get_prices(symbol, period, start_date, end_date)

fig = go.Figure(data=[go.Candlestick(x=data['time'],
                open=data['open'], high=data['high'],
                low=data['low'], close=data['close'])])

fig.update_layout(title=f'{symbol} Price Chart ({period})',
                  yaxis_title='Price (USD)',
                  xaxis_rangeslider_visible=False)

fig.show()