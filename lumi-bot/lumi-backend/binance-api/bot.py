import datetime
import time
from dataclasses import dataclass
from enum import Enum

import pandas as pd
import btalib


class TradeType(Enum):
    SPOT = 1
    FUTURE = 2


class OrderType(Enum):
    MARKET = 1
    LIMIT = 2


@dataclass
class TradeData:
    trade_type: TradeType
    order_type: OrderType
    pair: str  # Trading pair (e.g. BTCUSDT)
    quantity: float


class Bot:
    """Class responsible for the implementation of the trading bot"""

    # TODO Use adequate API in respect to the trade type (future or spot) - check out:
    #  https://python-binance.readthedocs.io/en/latest/binance.html

    def __init__(self, trade_data, client):
        self.trade_data = trade_data
        self.client = client
        self.entered = False
        self.order = None

    def get_data(self, interval, lookback_min):
        frame = pd.DataFrame(
            self.client.get_historical_klines(self.trade_data.pair, interval, lookback_min + ' min ago UTC'))
        frame = frame.iloc[:, :6]
        frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        frame = frame.set_index('Time')
        frame.index = pd.to_datetime(frame.index, unit='ms')
        frame = frame.astype(float)

        return frame

    def start(self, symbol, qty):
        while True:
            if not self.entered:
                self.buy()
                self.entered = True

            else:
                self.sell()
                self.entered = False

            time.sleep(5)  # 5 sec delay

    def buy(self):
        """Function implementing the buy strategy"""

        data = self.get_data(self.trade_data.pair, '1m', '30')
        cumulret = (data.Open.pct_change() + 1).cumprod() - 1

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
            sincebuyret = (sincebuy.Open.pct_change() + 1).cumprod() - 1

            if sincebuyret[-1] > 0.0015 or sincebuyret[-1] < -0.0015:
                # order = self.client.create_order(symbol=self.trade_data.pair, side='SELL', type=self.trade_data.type, quantity=self.trade_data.quantity)
                # print(order)

                print(datetime.datetime.now() + '\t-\tSell request created')

    def evaluate_sma(self, timeframe):
        timestamp = self.client._get_earliest_valid_timestamp(self.trade_data.pair, '1h')
        bars = self.client.get_historical_klines(self.trade_data.pair, '1h', timestamp, limit=1000)
        for line in bars:
            del line[6:]
        btc_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
        btc_df.set_index('date', inplace=True)
        btc_df.index = pd.to_datetime(btc_df.index, unit='ms')
        # calculate 20 moving average using Pandas
        btc_df['20sma'] = btc_df.close.rolling(5).mean()
        print(btc_df)
        # create sma and attach as column to original df
        sma = btalib.sma(btc_df.close)
        print(sma.df)
        btc_df['sma'] = btalib.sma(btc_df.close, period=20).df
        print(btc_df.tail())
        # rsi = btalib.rsi(btc_df)
        # print(rsi.df.rsi[-1])
