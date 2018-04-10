'''
Nasdaq Stock
Stock data extractory

To Use:
ticker = 'xxx'
stock_data = nasdaq_stock.stock(ticker)
'''
import requests
from lxml import html
import datetime


bidask = '//*[@id="left-column-div"]/div[1]/div[1]/div/div[1]/div[2]/text()'
highlow = '//*[@id="left-column-div"]/div[1]/div[1]/div/div[2]/div[2]/text()'
vol = '//*[@id="left-column-div"]/div[1]/div[1]/div/div[3]/div[2]/text()'
previousclose = '//*[@id="left-column-div"]/div[1]/div[1]/div/div[5]/div[2]/text()'
marketcap = '//*[@id="left-column-div"]/div[1]/div[2]/div/div[1]/div[2]/text()'

def stock(ticker):
    '''
    Retrieves stock ticker informantion.

    :param ticker: Valid nasdaq stock ticker.
    :return: Dictionary of stock information.
    '''
    url = 'https://www.nasdaq.com/symbol/{ticker}'.format(ticker=ticker)
    html_data = requests.get(url)
    NAS = False
    if html_data.status_code == 200:
        data = html.fromstring(html_data.content)
        try:
            check = data.xpath('//*[@id="left-column-div"]/div[1]/text()')
            for item in check:
                if item.find('This is an unknown symbol.')>0:
                    NAS = True
                    print('{tic} is not a vaild stock'.format(tic=ticker))
                    return (False)
        except:
            return (False)
        if NAS == False:
            try:
                Stock = ticker.upper()
                today = datetime.date.today().strftime('%B %d %Y')
                time = datetime.datetime.now().strftime('%H:%M:%S')
                rd_bid_ask = data.xpath(bidask)
                rd_high_low = data.xpath(highlow)
                rd_vol = data.xpath(vol)
                rd_previous_close = data.xpath(previousclose)
                rd_market_cap = data.xpath(marketcap)

                data_bid_ask = rd_bid_ask[0].strip()
                data_high_low = rd_high_low[0].strip()
                data_vol = rd_vol[0].strip()
                data_previous_close = rd_previous_close[0].strip()
                data_market_cap = rd_market_cap[0].strip()

                volume = data_vol.replace(',', '')
                previous_close = data_previous_close[2:]
                market_cap = data_market_cap.replace(',', '')

                if data_bid_ask.find('N/A')>=0:
                    bid = previous_close
                    ask = 'None'
                elif data_bid_ask.find('$')>=0:
                    data_array = data_bid_ask.split('/')
                    bid = data_array[0][2:]
                    ask = data_array[1][3:]
                else:
                    bid = 'None'
                    ask = 'None'

                if data_high_low.find('$')==-1:
                    high = 'None'
                    low = 'None'
                elif data_high_low.find('$')>=0:
                    data_array = data_high_low.split('/')
                    high = data_array[0][2:]
                    low = data_array[1][3:]
                else:
                    high = 'None'
                    low = 'None'

                print('***** '+Stock+' *****')
                print('Date: '+today)
                print('Time: '+time)
                print('Price: '+bid)
                print('Ask: '+ask)
                print('High: '+high)
                print('Low: '+low)
                print('Previous Close: ' + previous_close)
                print('Volume: '+volume)
                print('Market Cap: '+market_cap)

                s_dict = dict(ticker=Stock,date=today,time=time,price=bid,ask=ask,high=high,low=low,previous_close=previous_close,volume=volume,market_cap=market_cap)
                return s_dict
            except:
                return (False)

    else:
        print('Connection Not Found')
        return (False)

def main():
    ticker = input('Input Ticker: ')
    ticker_obj = stock(ticker)

if __name__ == '__main__':
    main()