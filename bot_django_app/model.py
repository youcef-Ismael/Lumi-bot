from bot import Bot


class Model:
    def __init__(self, trade_data, client):
        self.bot = Bot(trade_data, client)

    # TODO insert methods here that communicate with the Bot according to the trade data
