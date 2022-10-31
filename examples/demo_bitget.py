from cryptofeed import FeedHandler
from cryptofeed.exchanges import Bitget
from cryptofeed.defines import TRADES, TICKER


async def ticker(t, receipt_timestamp):
    print(t)


async def trade(t, receipt_timestamp):
    print(t)


def main():
    f = FeedHandler()
    f.add_feed(Bitget(symbols=['BTC-USDT'], channels=[TRADES, TICKER], callbacks={TICKER: ticker, TRADES: trade}))

    f.run()


if __name__ == '__main__':
    main()