import pandas as pd

from dataclasses import dataclass
from time import ctime
from binance import Client, BinanceSocketManager
from bot import TradeType, TradeData, OrderType

@dataclass
class Keys:
    api_key: str
    api_secret: str

class API:
    def __init__(self, keys, paper=True):        
        self.socket = None

        self.client = Client(keys.api_key, keys.api_secret)

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
        frame.Time = pd.to_datetime(frame.Time, unit = 'ms')

        return frame

    def get_asset_balance(self, asset):
        return self.client.get_asset_balance(asset=asset)

    def create_order(self, symbol, side, order_type, quantity):  # might be redundant
        self.client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)

    def futures_account_transfer(self, asset, amount, f_type, timestamp=ctime()):
        self.client.futures_account_transfer(asset=asset, amount=amount, type=f_type, timestamp=timestamp)




class Controller:
    """Class that communicates with the view (frontend) and model (trading bot)"""

    # TODO implement methods communicating with the frontend (Django) and, in turn, with the model

    def __init__(self):
        print()
        
