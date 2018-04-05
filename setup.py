from distutils.core import setup

long_description_text = "Nasdaq Stock: Stock data retriever\n \
=========================                  \n \
How to use                                 \n \
---------------                            \n \
>>>from nasdaq_stock import nasdaq_stock as ns\n \
or\n \
>>>from nasdaq_stock import nasdaq_stock   \n \
>>>nasdaq_stock.stock(‘spyd’)              \n \
or\n \
>>>spyd = nasdaq_stock.stock(‘spyd’)       \n \
\n \
This will return string data and a dictionary of that data.\n \
Current data fields are:                   \n \
ticker: The stock or id of that ticker.    \n \
date: The date when the stock was queried. \n \
time: The time when the stock was taken. This can be helpful if you are trying to do minute by minute data gathering\n \
price: The current price or bid price      \n \
ask: The current ask price                 \n \
high: The high of the day                  \n \
low: The low of the day                    \n \
previous_close: The previous closing form the last day. Not to be confused with last ask price\n \
volume: Volume of shares for the current day. \n \
market_cap: Market cap of the stock. i.e. dollar amount currently vested in stock\n \
"

setup(
  name = 'nasdaq_stock',
  packages = ['nasdaq_stock'],
  version = '0.0.2',
  description = 'nasdaq stock retriever',
  long_description = long_description_text
  author = 'George Shen',
  author_email = 'georgejs.arch@gmail.com',
  url = 'https://github.com/georgejs/nasdaq_stock',
  download_url = 'https://github.com/georgejs/nasdaq_stock/archive/0.0.2.tar.gz',
  keywords = ['stock', 'nasdaq', 'stock retriever', 'nasdaq stock'],
  classifiers = [],
)