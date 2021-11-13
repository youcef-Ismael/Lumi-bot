import time
import datetime
import pandas as pd

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
    pair: tuple
    pair_str: str  # Trading pair (e.g. BTCUSDT)
    quantity: float


class Bot:
    """Class responsible for the implementation of the trading bot"""

    # TODO Use adequate API in respect to the trade type (future or spot) - check out:
    #  https://python-binance.readthedocs.io/en/latest/binance.html

    def __init__(self, trade_data, api):
        self.trade_data = trade_data
        self.api = api
        self.entered = False
        self.order = None


    async def start(self):
        i = 0
        while True:
            # if not self.entered:
            #     self.buy()
            #     self.entered = True

            # else:
            #     self.sell()
            #     self.entered = False
            tmp = await self.api.get_data()
            print(tmp)

            time.sleep(5)  # 5 sec delay
            if i == 5:
                break
        
            i += 1

    def buy(self):
        """Function implementing the buy strategy"""
        period = '1m'
        data = self.get_dataframe(period)

        cumul_ret = (data.Open.pct_change() + 1).cumprod() - 1

        if cumul_ret[-1] < -0.002:
            if self.client.get_asset_balance(self.trade_data.pair[0]) >= self.trade_data.quantity:
                order = self.client.create_order(symbol=self.trade_data.pair_str, side='BUY', type=self.trade_data.type,
                                                 quantity=self.trade_data.quantity)
                self.orders.append(order)
                print(str(self.orders[-1]['transactTime']) + '\t-\tBuy request created')
            else:
                print('Not enough capital to execute trade')

        else:
            print(str(datetime.datetime.now()) + '\t-\tNo buy')

    def sell(self):
        """Function implementing the sell strategy"""
        period = '1m'
        data = self.get_dataframe(period)
        sincebuy = data.loc[data.index > pd.to_datetime(self.orders[-1]['transactTime'], unit='ms')]

        if len(sincebuy) > 0:
            sincebuy_ret = (sincebuy.Open.pct_change() + 1).cumprod() - 1

            if sincebuy_ret[-1] > 0.0015 or sincebuy_ret[-1] < -0.0015:
                order = self.client.create_order(symbol=self.trade_data.pair_str, side='SELL', type=self.trade_data.type,
                                                 quantity=self.trade_data.quantity)
                self.orders.append(order)
                print(str(datetime.datetime.now()) + '\t-\tSell request created')
            else:
                print(str(datetime.datetime.now()) + '\t-\tNo sell')

    def get_dataframe(self, timeframe='1h'):
        timestamp = self.client._get_earliest_valid_timestamp(self.trade_data.pair_str, '1d')
        klines = self.client.get_historical_klines(self.trade_data.pair_str, timeframe, timestamp, limit=1000)
        df = pd.DataFrame(klines)
        df = df.iloc[:, :6]
        df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        df.set_index('Date', inplace=True)
        df.index = pd.to_datetime(df.index, unit='ms')
        df = df.astype(float)
        return df

    def get_sma(self, period=20):
        df = self.get_dataframe()
        return df.Close.tail(period).mean()

    def get_ema(self, period=20):
        df = self.get_dataframe()
        ema = btalib.ema(df, period=period)
        return ema.df.ema[-1]

    def get_rsi(self, period=14):
        df = self.get_dataframe()
        if period > len(df) - 1:
            period = len(df) - 1
        rsi = btalib.rsi(df, period=period)
        return rsi.df.rsi[-1]

    def __get_highest_and_lowest_swing(self):
        highest_swing = -1
        lowest_swing = -1
        df = self.get_dataframe()
        for i in range(1, df.shape[0] - 1):
            if df['High'][i] > df['High'][i - 1] and df['High'][i] > df['High'][i + 1] and (
                    highest_swing == -1 or df['High'][i] > df['High'][highest_swing]):
                highest_swing = i
            if df['Low'][i] < df['Low'][i - 1] and df['Low'][i] < df['Low'][i + 1] and (
                    lowest_swing == -1 or df['Low'][i] < df['Low'][lowest_swing]):
                lowest_swing = i
        return highest_swing, lowest_swing

    def __get_max_and_min_lvl(self):
        hi, lo = self.__get_highest_and_lowest_swing()
        df = self.get_dataframe()
        max_level = df['High'][hi]
        min_level = df['Low'][lo]
        return max_level, min_level

    def get_fibonacci_ratio_lvls(self):
        max_level, min_level = self.__get_max_and_min_lvl()
        highest_swing, lowest_swing = self.__get_highest_and_lowest_swing()
        ratios = [0.236, 0.382, 0.618, 0.786]
        levels = []
        for ratio in ratios:
            if highest_swing > lowest_swing:  # Uptrend
                levels.append(max_level - (max_level - min_level) * ratios)
            else:  # Downtrend
                levels.append(min_level + (max_level - min_level) * ratios)
        return levels
