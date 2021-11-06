import model
import os
from dataclasses import dataclass

from binance.client import Client

from bot import TradeType, OrderType


@dataclass
class API:
    api_key: str
    api_secret: str


class Controller:
    """Class that communicates with the view (frontend) and trading bot model"""

    def __init__(self, trade_type: TradeType, order_type: OrderType, paper=True):
        self.api_key = os.environ.get('binance_api')
        self.api_secret = os.environ.get('binance_secret')
        self.api_data = API(self.api_key, self.api_secret)
        self.client = Client(self.api_data.api_key, self.api_data.api_secret)
        self.paper = paper
        if paper:
            self.client.API_URL = 'https://testnet.binance.vision/api'
        self.trade_type = trade_type
        self.order_type = order_type
        self.model = model.Model(trade_type, order_type, 'BTCUSDT', 0.001)

    # TODO implement methods communicating with the frontend (Django) and, in turn, with the model
