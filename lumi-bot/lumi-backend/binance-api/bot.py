import pandas as pd
import time
import datetime

from dataclasses import dataclass
from binance import Client


@dataclass
class API:
    api_key: str
    api_secret_key: str

@dataclass
class TradeData:
    type: str           # MARKET / LIMIT
    pair: str           # Trading pair (e.g. BTCUSDT)
    quantity: float


class Bot:
    """Class responsible for the implementation of the trading bot"""

    def __init__(self, api_data, trade_data):
        self.api_data = api_data
        self.trade_data = trade_data
        self.client = Client(self.api_data.api_key, self.api_data.api_secret_key)
        self.entried = False
        self.order = None

    def get_data(self, interval, lookback_min):
        frame = pd.DataFrame(self.client.get_historical_klines(self.trade_data.pair, interval, lookback_min + ' min ago UTC'))
        frame = frame.iloc[:, :6]
        frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        frame = frame.set_index('Time')
        frame.index = pd.to_datetime(frame.index, unit = 'ms')
        frame = frame.astype(float)

        return frame

    def start(self, symbol, qty):
        while True:
            if not self.entried:
                self.buy()
                self.entried = True

            else:
                self.sell()
                self.entried = False

            time.sleep(5)   # 5 sec delay

    def buy(self):
        """Function implementing the buy strategy"""

        data = self.get_data(self.trade_data.pair, '1m', '30')
        cumulret = (data.Open.pct_change() + 1). cumprod() - 1

        if cumulret[-1] < -0.002:
            # self.order = self.client.create_order(symbol=self.trade_data.pair, side='BUY', type=self.trade_data.type, quantity=self.trade_data.quantity)
            # print('Order: ' + order)
            
            print(datetime.datetime.now() + '\t-\tBuy request created')

        else:
            print(datetime.datetime.now() + '\t-\tNo trade')

    def sell(self):
        """Function implementing the sell strategy"""

        data = self.get_data(self.trade_data.pair, '1m', '30')
        sincebuy = data.loc[data.index > pd.to_datetime(self.order['transactTime'], unit='ms')]
        
        if len(sincebuy) > 0:
            sincebuyret = (sincebuy.Open.pct_change() + 1). cumprod() - 1
            
            if sincebuyret[-1] > 0.0015 or sincebuyret[-1] < -0.0015:
                # order = self.client.create_order(symbol=self.trade_data.pair, side='SELL', type=self.trade_data.type, quantity=self.trade_data.quantity)
                # print(order)

                print(datetime.datetime.now() + '\t-\tSell request created')