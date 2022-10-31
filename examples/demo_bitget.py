from cryptofeed import FeedHandler
from cryptofeed.exchanges import Bitget
from cryptofeed.defines import TRADES, TICKER, OPEN_INTEREST, FUNDING


async def ticker(t, receipt_timestamp):
    print(t)


async def trade(t, receipt_timestamp):
    print(t)

async def open_interest(t, receipt_timestamp):
    print(t)
    
async def funding(t, receipt_timestamp):
    print(t)


def main():
    f = FeedHandler()
    # f.add_feed(Bitget(symbols=['BTC-USDT-PERP', 'ETH-USDT-PERP', 'DOGE-USDT-PERP', 'SOL-USDT-PERP'], channels=[OPEN_INTEREST], callbacks={OPEN_INTEREST: open_interest}))
    f.add_feed(Bitget(symbols=['BTC-USDT-PERP', 'ETH-USDT-PERP', 'DOGE-USDT-PERP', 'SOL-USDT-PERP'], channels=[FUNDING], callbacks={FUNDING: funding}))
    # f.add_feed(Bitget(symbols=['BTC-USDT'], channels=[TRADES, TICKER], callbacks={TRADES: trade}))

    f.run()


if __name__ == '__main__':
    main()