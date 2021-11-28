from dataclasses import dataclass
from time import ctime

import pandas as pd
from binance import BinanceSocketManager, AsyncClient

from bot_django_app.bot import TradeType
from bot_django_app.model import Model


@dataclass
class Keys:
    api_key: str
    api_secret: str


class API:
    def __init__(self, keys, paper=True):
        self.socket = None

        self.client = AsyncClient(keys.api_key, keys.api_secret)

        self.paper = paper
        if self.paper:
            self.client.API_URL = 'https://testnet.binance.vision/api'

        self.socket_manager = BinanceSocketManager(self.client)

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
        return self.client.get_asset_balance(asset=asset)

    def futures_account_transfer(self, asset, amount, f_type, timestamp=ctime()):
        self.client.futures_account_transfer(asset=asset, amount=amount, type=f_type, timestamp=timestamp)


class Controller:
    """Class that communicates with the view (frontend) and model (trading bot)"""

    def __init__(self):
        self.model = None

    """
    @param api_key = str #from db
    @param api_secret = str #from db
    @param quantity = float
    @param pair = tuple(string, string)
    """
    def start(self, api_key, api_secret, quantity=0.001, pair=('BTC', 'USDT')):
        self.model = Model(Keys(api_key, api_secret))
        self.model.set_trade_data(trade_type=TradeType.SPOT, quantity=quantity, pair=pair)
        self.model.bot.start()

    def stop(self):
        self.model.bot.stop()
        self.model = None

    """
    @param quantity = float
    """
    def update_quantity(self, quantity):
        if self.model is not None:
            self.model.bot.set_trade_data(trade_data=TradeType.SPOT, quantity=quantity, pair=self.model.bot.trade_data.pair)
        else:
            print('Operation failed, model is None')

    """
    @param asset = string (e.g. 'BTC')
    """
    def get_asset_balance(self, asset):
        if self.model is not None:
            return self.model.api.client.get_asset_balance(asset=asset)
        else:
            print('Operation failed, model is None')