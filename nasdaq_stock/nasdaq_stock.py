'''
Nasdaq Stock
Stock data extractory
To Use:
ticker = 'xxx'
stock_data = nasdaq_stock.stock(ticker)
'''
import requests
from lxml import html
from lxml import etree
import datetime


price_xp = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]/text()'
range_xp = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[5]/td[2]/text()'
vol_xp = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[7]/td[2]/span/text()'
vol_avg_xp = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[8]/td[2]/span/text()'
previousclose_xp = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/span/text()'
marketcap_xp = '//*[@id="left-column-div"]/div[1]/div[2]/div/div[1]/div[2]/text()'

def stock(ticker):
    '''
    Retrieves stock ticker informantion.
    :param ticker: Valid nasdaq stock ticker.
    :return: Dictionary of stock information.
    '''
    ticker = ticker.upper()
    
    url = "https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch".format(ticker=ticker)
    
    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'cache-control': "no-cache"
    }
    
    response = requests.request("GET", url, headers=headers)
    today = datetime.date.today().strftime('%B %d %Y')
    time = datetime.datetime.now().strftime('%H:%M:%S')
    
    NAS = False
    if response.status_code == 200:    
        data = html.fromstring(response.content)
        #print(type(data))#Debug
        try:
            check = data.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1/text()')
            if len(check) > 0:
                NAS = False
            else:
                return (False)
        except:
            return (False)
        
        try:
            Stock = ticker.upper()
            today = datetime.date.today().strftime('%B %d %Y')
            time = datetime.datetime.now().strftime('%H:%M:%S')
            
            rd_bid_ask = data.xpath(price_xp)
            rd_high_low = data.xpath(range_xp)
            rd_vol = data.xpath(vol_xp)
            rd_vol_avg = data.xpath(vol_avg_xp)
            rd_previous_close = data.xpath(previousclose_xp)
            
            price = rd_bid_ask[0].strip()
            ask = rd_bid_ask[0].strip()
            volume = rd_vol[0].strip().strip().replace(',','')
            previous_close = rd_previous_close[0].strip()

        except:
            return (False)
        try:
            high_low = rd_high_low[0].split(' - ')
        except:
            high_low = ['0.0','0.0']
        
        try:
            high = [float(high_low[1].strip().replace(',',''))]
            low = [float(high_low[0].strip().replace(',',''))]
        except:
            high = ['0.0']
            low = ['0.0']
        
        stock_dic = {'ticker':str(Stock), \
                'date':today, \
                'time':time, \
                'price':str(price), \
                'ask':str(ask), \
                'range_val':str(rd_high_low[0]), \
                'vol':str(volume), \
                'vol_avg':str(rd_vol_avg[0].replace(',','')), \
                'previous_close':str(previous_close), \
                'high':str(high[0]), \
                'low':str(low[0])}
        
        print(stock_dic)
        
    else:
        stock_dic = {'ticker': 'Not-Available', \
                     'date': today, \
                     'time': time, \
                     'price': 'Not-Available', \
                     'ask': 'Not-Available', \
                     'range_val': str('Not-Available'), \
                     'vol': 'Not-Available', \
                     'vol_avg': str('Not-Available'), \
                     'previous_close': str('Not-Available'), \
                     'high': str('Not-Available'), \
                     'low': str('Not-Available')}
    return stock_dic
    
def print_stock(dic_stock):
    print('Price          :'+dic_stock.get('price'))
    print('Range          :'+dic_stock.get('range_val'))
    print('Volume         :'+dic_stock.get('vol'))
    print('Avg Volume     :'+dic_stock.get('vol_avg'))
    print('Previous Close :'+dic_stock.get('previous_close'))
    print('High           :'+dic_stock.get('high'))
    print('Low            :'+dic_stock.get('low'))
    
def main():
    ticker = input('Ticker: ')
    report = stock(ticker)
    print(report.keys())
    print_stock(report)

    
if __name__ == '__main__':
    main()
