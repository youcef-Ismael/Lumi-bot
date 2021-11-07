
import pandas as pd
from binance import Client, BinanceSocketManager

class API:
    def __init__(self, key, secret_key):
        self.key = key
        self.secret_key = secret_key
        self.socket_manager = BinanceSocketManager(Client(self.key, self.secret_key))
        self.socket = None

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

        