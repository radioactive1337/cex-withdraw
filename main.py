from Exchanges import Exchanges

if __name__ == '__main__':
    print('1. Bybit\n2. Binance')
    num = input('Choose num of cex: ')
    currency = input('Choose currency: ')
    network = input('Choose network: ')
    amount = input('Amount to withdraw: ')
    if int(num) == 1:
        Exchanges.bybit_withdraw(float(amount), network, currency)
    else:
        Exchanges.binance_withdraw(float(amount), network, currency)
