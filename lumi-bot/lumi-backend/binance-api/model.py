from bot import TradeData, Bot


class Model:
    def __init__(self, client, trade_type, order_type, pair, quantity):
        self.trade_data = TradeData(trade_type, order_type, pair, quantity)
        self.bot = Bot(self.trade_data, client)

    # TODO insert methods here that communicate with the Bot according to the trade data
