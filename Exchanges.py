import datetime
import os

import ccxt
from dotenv import load_dotenv

load_dotenv()
bybit_api_key = os.getenv('BYBIT_API_KEY')
bybit_api_secret = os.getenv('BYBIT_API_SECRET')
now = datetime.datetime.now()
symbolWithdraw = "BNB"
network = "BSC"
proxy_server = ''  # https://login:password@IP:port


class Exchanges:

    @staticmethod
    def bybit_withdraw(address, amount, wallet):
        bybit = ccxt.bybit(
            {
                'apiKey': bybit_api_key,
                'secret': bybit_api_secret
            }
        )
        try:
            bybit.withdraw(
                code=symbolWithdraw,
                amount=amount,
                address=address,
                tag=None,
                params={
                    "forceChain": 1,
                    "network": network
                }
            )
            print(f'\n{now}\tINFO [ByBit Withdraw {amount} {symbolWithdraw}] ', flush=True)
            print(f'\n{now}\t{wallet} {address}', flush=True)
        except Exception as error:
            print(f'\n{now}\t[ByBit Withdraw error {amount} {symbolWithdraw}]: {error} ', flush=True)
            print(f'\n{now}\t{wallet} {address}', flush=True)
