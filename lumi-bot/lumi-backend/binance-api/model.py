import asyncio
import controller

from bot import TradeData, Bot, TradeType, OrderType
from controller import API, Keys

from personal_data import testnet_api_key, testnet_secret_key


class Model:
    def __init__(self, keys):
        self.api = API(keys)
        self.bot = Bot(self.api)

        self.orders = {}
        self.open_trades = {}  # to keep track of futures, for this we need persistence # (transaction_time, order) pairs

    # TODO insert methods here that communicate with the Bot according to the trade data

    def start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(model.bot.start())
        loop.close()

    def set_trade_data(self, trade_type, quantity, pair: tuple = ('BTC', 'USDT')):
        self.pair_str = pair[0] + pair[1]
        self.trade_data = TradeData(trade_type, pair, self.pair_str, quantity)
        self.bot.set_trade_data(self.trade_data)




model = Model(Keys(testnet_api_key, testnet_secret_key))
model.set_trade_data(trade_type=TradeType.SPOT, quantity=0.001)
model.start()