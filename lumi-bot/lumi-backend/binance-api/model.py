import asyncio

from bot import TradeData, Bot, TradeType, OrderType
from api import API

from personal_data import api_key, api_secret_key


class Model:
    def __init__(self, api, trade_type, order_type, pair, interval, lookback):
        self.api = api
        self.trade_data = TradeData(trade_type, order_type, pair, interval, lookback)
        self.bot = Bot(self.trade_data, self.api)

    # TODO insert methods here that communicate with the Bot according to the trade data




api = API(api_key, api_secret_key)
api.set_pair('BTCUSD')
model = Model(api, TradeType.SPOT, OrderType.MARKET, 'BTCUSD', 1, 30)

loop = asyncio.get_event_loop()
loop.run_until_complete(model.bot.start())
loop.close()