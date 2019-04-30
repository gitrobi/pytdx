from pytdx.hq import TdxHq_API, TDXParams
from pytdx.exhq import TdxExHq_API, TDXParams
import time


def test_hq():
    api = TdxHq_API(multithread=False)
    with api.connect(time_out=30):
        for i in range(100):
            stocks = api.get_security_quotes([(0, "000001"), (1, "600300")])
            #print(stocks)
            #print(type(stocks))
            print(stocks[0].get('code'), stocks[0].get('price'), stocks[0].get('bid1'),stocks[0].get('bid_vol1'), stocks[0].get('ask1'), stocks[0].get('ask_vol1'))
            time.sleep(1.5)


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


#test_hq()
test_exhq()