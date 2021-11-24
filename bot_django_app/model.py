import os

from bot import TradeData, Bot, TradeType, OrderType
from controller import API, Keys


def start():
    model.bot.start()


class Model:
    def __init__(self, keys):
        self.api = API(keys)
        self.bot = Bot(self.api)

        self.orders = {}
        self.open_trades = {}  # to keep track of futures, for this we need persistence # (transaction_time, order) pairs

    # TODO insert methods here that communicate with the Bot according to the trade data

    def set_trade_data(self, trade_type: TradeType, quantity: float, pair: tuple = ('BTC', 'USDT')):
        pair_str = pair[0] + pair[1]
        trade_data = TradeData(trade_type, OrderType.MARKET, pair, pair_str, quantity)
        self.bot.set_trade_data(trade_data)


model = Model(Keys(os.environ.get('binance_api'), os.environ.get('binance_secret')))
model.set_trade_data(trade_type=TradeType.SPOT, quantity=0.001, pair=('BTC', 'USDT'))
# print(model.api.get_asset_balance('BTC'))
start()
