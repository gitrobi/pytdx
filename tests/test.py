from pytdx.hq import TdxHq_API, TDXParams
from pytdx.exhq import TdxExHq_API, TDXParams
import time


def test_hq():
    import pprint

    api = TdxHq_API(multithread=False)
    with api.connect(time_out=30):
        for i in range(100):
            stocks = api.get_security_quotes([(0, "000001"), (1, "600993")])
            #print(stocks)
            #print(type(stocks))
            print(stocks[1].get('code'), stocks[1].get('price'), stocks[1].get('bid1'),stocks[1].get('bid_vol1'), stocks[1].get('ask1'), stocks[1].get('ask_vol1'))


            #data = api.get_transaction_data(TDXParams.MARKET_SH, '601818', 0, 100)
            #pprint.pprint(data)
            #print('time:{},price:{},vol:{},buyorsell:{}'.format(data[0].get('time'), data[0].get('price'), data[0].get('vol'), data[0].get('buyorsell')))

            time.sleep(1.5)

            # data = api.get_history_transaction_data(TDXParams.MARKET_SZ, '123001', 0, 10000, 20190430)
            # print(data)

def test_exhq():
    # symbol_params = [
    #     [47, "IF1709"],
    #     [8, "10000889"],
    #     [31, "00020"],
    #     [47, "IFL0"],
    #     [31, "00700"]
    # ]

    symbol_params = [[47, 'IF1905']]

    api = TdxExHq_API(auto_retry=True)
    with api.connect('220.248.233.5', 7721, time_out=30):
        #data = api.get_markets()
        #print(data)

        for i in range(100):
            stocks = api.get_instrument_quote(47, 'IF1905')
            # print(stocks)
            print(stocks[0].get('code'), stocks[0].get('price'), stocks[0].get('bid1'), stocks[0].get('bid_vol1'),
                  stocks[0].get('ask1'), stocks[0].get('ask_vol1'))
            time.sleep(1.1)


test_hq()
#test_exhq()