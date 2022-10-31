'''
Copyright (C) 2017-2022 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
import asyncio
from decimal import Decimal
import logging

from yapic import json

from cryptofeed.defines import OPEN_INTEREST
from cryptofeed.exchange import RestExchange
from cryptofeed.util.time import timedelta_str_to_sec
from cryptofeed.types import OrderBook, Candle


LOG = logging.getLogger('feedhandler')


class BitgetRestMixin(RestExchange):
    api = "https://api.bitget.com/api"
    rest_channels = (
        OPEN_INTEREST,
    )
    
class BitgetFuturesRestMixin(RestExchange):
    api = "https://api.bitget.com/api"
    rest_channels = (
        OPEN_INTEREST,
    )
