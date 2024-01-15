import datetime
import os

import ccxt
from dotenv import load_dotenv

load_dotenv()
bybit_api_key = os.getenv('BYBIT_API_KEY')
bybit_api_secret = os.getenv('BYBIT_API_SECRET')
binance_api_key = os.getenv('BINANCE_API_KEY')
binance_api_secret = os.getenv('BINANCE_API_SECRET')

proxy = os.getenv('PROXY')
address = os.getenv('ADDRESS')
now = datetime.datetime.now()


class Exchanges:

    @staticmethod
    def bybit_withdraw(amount, network, currency):
        bybit = ccxt.bybit(
            {
                'apiKey': bybit_api_key,
                'secret': bybit_api_secret
            }
        )
        try:
            bybit.withdraw(
                code=currency,
                amount=amount,
                address=address,
                tag=None,
                params={
                    "forceChain": 1,
                    "network": network
                }
            )
            print(f'\n{now}\tINFO [ByBit Withdraw {amount} {currency}] ', flush=True)
            print(f'\n{now}\t{address}', flush=True)
        except Exception as error:
            print(f'\n{now}\t[ByBit Withdraw error {amount} {currency}]: {error} ', flush=True)
            print(f'\n{now}\t{address}', flush=True)

    @staticmethod
    def binance_withdraw(amount, network, currency):
        binance = ccxt.binance(
            {
                'apiKey': binance_api_key,
                'secret': binance_api_secret,
                'enableRateLimit': True,
                'proxies': proxy,
                'options': {
                    'defaultType': 'spot'
                }
            }
        )
        try:
            binance.withdraw(
                code=currency,
                amount=amount,
                address=address,
                tag=None,
                params={
                    "network": network
                }
            )
            print(f'\n{now}\tINFO [Binance Withdraw {amount} {currency}]', flush=True)
            print(f'\n{now}\t{address}', flush=True)
        except Exception as error:
            print(f'\n{now}\t[Binance Withdraw error {amount} {currency}]: {error}', flush=True)
            print(f'\n{now}\t{address}', flush=True)
