from bot_django_app.bot import TradeType
from bot_django_app.model import Model, Keys

# The BOT


class Controller:
    """Class that communicates with the view (frontend) and model (trading bot)"""

    def __init__(self, api_key, api_secret):
        self.model = Model(Keys(api_key, api_secret))

    """
    @param quantity = float
    @param pair = tuple(string, string)
    """

    def start(self, quantity=0.001, pair=('BTC', 'USDT')):
        self.model.set_trade_data(
            trade_type=TradeType.SPOT, quantity=quantity, pair=pair)
        self.model.bot.start()

    def stop(self):
        self.model.bot.stop()
        # self.model = None

    """
    @param quantity = float
    """

    def update_quantity(self, quantity):
        self.model.bot.set_trade_data(trade_data=TradeType.SPOT, quantity=quantity,
                                      pair=self.model.bot.trade_data.pair)

    def get_balances_for_assets(self):
        assets = ["BTC", "LTC", "ETH", "NEO", "BNB", "QTUM", "EOS", "SNT", "BNT", "GAS", "BCC", "USDT", "HSR", "OAX",
                  "DNT",
                  "MCO", "ICN", "ZRX", "OMG", "WTC", "YOYO", "LRC", "TRX", "SNGLS", "STRAT", "BQX", "FUN", "KNC", "CDT",
                  "XVG",
                  "IOTA", "SNM", "LINK", "CVC", "TNT", "REP", "MDA", "MTL", "SALT", "NULS", "SUB", "STX", "MTH", "ADX",
                  "ETC",
                  "ENG", "ZEC", "AST", "GNT", "DGD", "BAT", "DASH", "POWR", "BTG", "REQ", "XMR", "EVX", "VIB", "ENJ",
                  "VEN",
                  "ARK", "XRP", "MOD", "STORJ", "KMD", "RCN", "EDO", "DATA", "DLT", "MANA", "PPT", "RDN", "GXS", "AMB",
                  "ARN",
                  "BCPT", "CND", "GVT", "POE", "BTS", "FUEL", "XZC", "QSP", "LSK", "BCD", "TNB", "ADA", "LEND", "XLM",
                  "CMT",
                  "WAVES", "WABI", "GTO", "ICX", "OST", "ELF", "AION", "WINGS", "BRD", "NEBL", "NAV", "VIBE", "LUN",
                  "TRIG",
                  "APPC", "CHAT", "RLC", "INS", "PIVX", "IOST", "STEEM", "NANO", "AE", "VIA", "BLZ", "SYS", "RPX",
                  "NCASH",
                  "POA", "ONT", "ZIL", "STORM", "XEM", "WAN", "WPR", "QLC", "GRS", "CLOAK", "LOOM", "BCN", "TUSD",
                  "ZEN", "SKY",
                  "THETA", "IOTX", "QKC", "AGI", "NXS", "SC", "NPXS", "KEY", "NAS", "MFT", "DENT", "IQ", "ARDR", "HOT",
                  "VET",
                  "DOCK", "POLY", "VTHO", "ONG", "PHX", "HC", "GO", "PAX", "RVN", "DCR", "USDC", "MITH", "BCHABC",
                  "BCHSV",
                  "REN", "BTT", "USDS", "FET", "TFUEL", "CELR", "MATIC", "ATOM", "PHB", "ONE", "FTM", "BTCB", "USDSB",
                  "CHZ",
                  "COS", "ALGO", "ERD", "DOGE", "BGBP", "DUSK", "ANKR", "WIN", "TUSDB", "COCOS", "PERL", "TOMO", "BUSD",
                  "BAND",
                  "BEAM", "HBAR", "XTZ", "NGN", "DGB", "NKN", "GBP", "EUR", "KAVA", "RUB", "UAH", "ARPA", "TRY", "CTXC",
                  "AERGO",
                  "BCH", "TROY", "BRL", "VITE", "FTT", "AUD", "OGN", "DREP", "BULL", "BEAR", "ETHBULL", "ETHBEAR",
                  "XRPBULL",
                  "XRPBEAR", "EOSBULL", "EOSBEAR", "TCT", "WRX", "LTO", "ZAR", "MBL", "COTI", "BKRW", "BNBBULL",
                  "BNBBEAR",
                  "HIVE", "STPT", "SOL", "IDRT", "CTSI", "CHR", "BTCUP", "BTCDOWN", "HNT", "JST", "FIO", "BIDR", "STMX",
                  "MDT",
                  "PNT", "COMP", "IRIS", "MKR", "SXP", "SNX", "DAI", "ETHUP", "ETHDOWN", "ADAUP", "ADADOWN", "LINKUP",
                  "LINKDOWN", "DOT", "RUNE", "BNBUP", "BNBDOWN", "XTZUP", "XTZDOWN", "AVA", "BAL", "YFI", "SRM", "ANT",
                  "CRV",
                  "SAND", "OCEAN", "NMR", "LUNA", "IDEX", "RSR", "PAXG", "WNXM", "TRB", "EGLD", "BZRX", "WBTC", "KSM",
                  "SUSHI",
                  "YFII", "DIA", "BEL", "UMA", "EOSUP", "TRXUP", "EOSDOWN", "TRXDOWN", "XRPUP", "XRPDOWN", "DOTUP",
                  "DOTDOWN",
                  "NBS", "WING", "SWRV", "LTCUP", "LTCDOWN", "CREAM", "UNI", "OXT", "SUN", "AVAX", "BURGER", "BAKE",
                  "FLM",
                  "SCRT", "XVS", "CAKE", "SPARTA", "UNIUP", "UNIDOWN", "ALPHA", "ORN", "UTK", "NEAR", "VIDT", "AAVE",
                  "FIL",
                  "SXPUP", "SXPDOWN", "INJ", "FILDOWN", "FILUP", "YFIUP", "YFIDOWN", "CTK", "EASY", "AUDIO", "BCHUP",
                  "BCHDOWN",
                  "BOT", "AXS", "AKRO", "HARD", "KP3R", "RENBTC", "SLP", "STRAX", "UNFI", "CVP", "BCHA", "FOR", "FRONT",
                  "ROSE",
                  "HEGIC", "AAVEUP", "AAVEDOWN", "PROM", "BETH", "SKL", "GLM", "SUSD", "COVER", "GHST", "SUSHIUP",
                  "SUSHIDOWN",
                  "XLMUP", "XLMDOWN", "DF", "JUV", "PSG", "BVND", "GRT", "CELO", "TWT", "REEF", "OG", "ATM", "ASR",
                  "1INCH",
                  "RIF", "BTCST", "TRU", "DEXE", "CKB", "FIRO", "LIT", "PROS", "VAI", "SFP", "FXS", "DODO", "AUCTION",
                  "UFT",
                  "ACM", "PHA", "TVK", "BADGER", "FIS", "OM", "POND", "ALICE", "DEGO", "BIFI", "LINA"]

        balances_assets = {}

        for asset in assets:
            amount = self.model.api.get_asset_balance(asset)
            if amount is not None:
                balances_assets[asset] = amount['free']
        return balances_assets


# TO IMPLEMENT
def get_balances_for_assets(api_key, api_secret):
    pass
