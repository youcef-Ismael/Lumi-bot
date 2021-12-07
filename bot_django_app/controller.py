from typing import Tuple, Dict
from bot_django_app.bot import TradeType
from bot_django_app.model import Model, Keys

models = {}

def start(api_key: str, secret_key, quantity: float = 0.001, pair: Tuple[str, str] = ('BTC', 'USDT')) -> None:
    
    # If not initialized model
    if api_key not in models:
        models[api_key] = Model(Keys(api_key, secret_key))

    models[api_key].set_trade_data(trade_type=TradeType.SPOT, quantity=quantity, pair=pair)
    models[api_key].bot.start()

def stop(api_key: str) -> None:

    if api_key in models:
        models[api_key].bot.stop()
    
def update_quantity(api_key: str, quantity: float) -> None:
    
    if api_key in models:
        models[api_key].bot.set_trade_data(trade_data=TradeType.SPOT, quantity=quantity, pair=models[api_key].bot.trade_data.pair)

def get_balances_for_assets(api_key: str) -> Dict[str, float]:
    assets = ["BTC", "LTC", "ETH", "USDT"]

    balances_assets = {}

    for asset in assets:
        amount = models[api_key].api.get_asset_balance(asset)
        if amount is not None:
            balances_assets[asset] = amount['free']
    return balances_assets


# start('cpFw7Z8Q8AREBMt2JQ98K56Vwl8oDuZ930C1v2SpcOV72pS69Paumop8dST7OGXK', 'q2aDRz47amumZT5AtEAFotGq2JgyJz3bBnkqYyuwgM4HxIFEKt7zLI7WACt4AGhX')