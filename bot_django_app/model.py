import os
import pandas as pd
import asyncio
from dataclasses import dataclass
from time import ctime
from binance import BinanceSocketManager
from binance.client import Client

from .bot import TradeData, Bot, TradeType, OrderType

# create a new event loop


def create_new_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return asyncio.get_event_loop()


def start():
    model.bot.start()


@dataclass
class Keys:
    api_key: str
    api_secret: str


class API:
    def __init__(self, keys: Keys, paper=True):
        self.socket = None
        self.client = Client(keys.api_key, keys.api_secret)

        self.paper = paper
        if self.paper:
            self.client.API_URL = 'https://testnet.binance.vision/api'
        # i added the second argument loop to create a new event loop other than the thread main loop
        self.socket_manager = BinanceSocketManager(
            self.client, loop=create_new_loop())

    def set_pair(self, pair):
        self.socket = self.socket_manager.trade_socket(pair)

    async def get_data(self):
        await self.socket.__aenter__()
        data = await self.socket.recv()

        return self.clean_data(data)

    def clean_data(self, data):
        frame = pd.DataFrame([data])
        frame = frame.loc[:, ['s', 'E', 'p']]
        frame.columns = ['Pair', 'Time', 'Price']
        frame.Price = frame.Price.astype(float)
        frame.Time = pd.to_datetime(frame.Time, unit='ms')

        return frame

    def get_asset_balance(self, asset):
        if self.client.get_asset_balance(asset=asset) is not None:
            return self.client.get_asset_balance(asset=asset)
        return None

    def futures_account_transfer(self, asset, amount, f_type, timestamp=ctime()):
        self.client.futures_account_transfer(
            asset=asset, amount=amount, type=f_type, timestamp=timestamp)


class Model:
    def __init__(self, keys: Keys):
        self.api = API(keys)
        self.bot = Bot(self.api)

    # TODO insert methods here that communicate with the Bot according to the trade data

    def set_trade_data(self, trade_type: TradeType, quantity: float, pair: tuple = ('BTC', 'USDT')):
        pair_str = pair[0] + pair[1]
        trade_data = TradeData(
            trade_type, OrderType.MARKET, pair, pair_str, quantity)
        self.bot.set_trade_data(trade_data)


model = Model(Keys(os.environ.get('binance_api'),
              os.environ.get('binance_secret')))
model.set_trade_data(trade_type=TradeType.SPOT,
                     quantity=0.001, pair=('BTC', 'USDT'))
print(model.api.get_asset_balance('BTC'))
start()
