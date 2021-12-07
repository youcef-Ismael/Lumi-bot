import unittest
import asyncio

from model import API, Keys
from bot import TradeData, Bot, TradeType, OrderType


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.api = API(Keys('cpFw7Z8Q8AREBMt2JQ98K56Vwl8oDuZ930C1v2SpcOV72pS69Paumop8dST7OGXK', 'q2aDRz47amumZT5AtEAFotGq2JgyJz3bBnkqYyuwgM4HxIFEKt7zLI7WACt4AGhX'))
        self.api.set_pair('BTCUSDT')

    def test_get_asset_balance(self):
        self.assertTrue(self.api.get_asset_balance('BTC'))

    def test_clean_data(self):
        d = {'e': 'trade', 'E': 1638737378351, 's': 'BTCUSDT', 't': 1178878007, 'p': '48914.74000000', 'q': '0.07647000', 'b': 8524868221, 'a': 8524868345, 'T': 1638737378351, 'm': True, 'M': True}
        df_clean = self.api.clean_data(d)
        
        with self.assertRaises(TypeError):
            self.__check_dataframe(df_clean)

    def test_get_data(self):
        loop = asyncio.get_event_loop()

        data = loop.run_until_complete(self.api.get_data())
        
        with self.assertRaises(TypeError):
            self.__check_dataframe(data)

    def __check_dataframe(frame):
        for col in frame:
                if col not in ['Pair', 'Time', 'Price']:
                    raise TypeError()


# class BotTestCase(unittest.TestCase):
#     def setUp(self):
#         self.bot = Bot(API(Keys('cpFw7Z8Q8AREBMt2JQ98K56Vwl8oDuZ930C1v2SpcOV72pS69Paumop8dST7OGXK', 'q2aDRz47amumZT5AtEAFotGq2JgyJz3bBnkqYyuwgM4HxIFEKt7zLI7WACt4AGhX')))
#         trade_data = TradeData(TradeType.SPOT, OrderType.MARKET, ('BTC', 'USDT'), 'BTCUSDT', 0.01)
#         self.bot.set_trade_data(trade_data)

#     def test_populate_df(self):
#         loop = asyncio.get_event_loop()
#         asyncio.ensure_future(self.bot.populate_df(), loop=loop)
#         asyncio.ensure_future(self.__stop(), loop=loop)
#         loop.run_forever()

#         self.assertTrue(self.bot.df.shape[0] > 0)

#     async def __stop(self):
#         await asyncio.sleep(60)
#         self.bot.stop()

if __name__ == '__main__':
    unittest.main()