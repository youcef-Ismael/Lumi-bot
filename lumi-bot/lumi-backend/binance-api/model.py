from personal_data import *         # Stores the personal information for the Binance API
from bot import API, TradeData, Bot

api_data = API(api_key, api_private_key)
trade_data = TradeData('MARKET', 'BTCUSDT', 0.001)

bot = Bot(api_data, trade_data)
print(bot.get_data('1m', '30'))


# bot.start()