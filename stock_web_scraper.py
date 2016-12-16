from __future__ import print_function

import requests
from bs4 import BeautifulSoup
import json

url = "http://banggia2.ssi.com.vn/AjaxWebService.asmx/GetHoseStockQuoteInit"

payload = {'key':'value'}
##payload = {'VersionId': 0}
r = requests.post(url, data=payload)

soup = BeautifulSoup(r.text, "html.parser")
contents = soup.find('string').string[9:]

array_stocks = contents.split("#")

## +/-
##def Percent(MatchPrice, PriorPrice):
##    if MatchPrice is None:
##        return None
##    elif PriorPrice is None:
##        return MatchPrice
##    else:
##        return MatchPrice - PriorPrice

def Percent(MatchPrice, PriorPrice):
    if MatchPrice is '':
        return ''
    elif PriorPrice is '':
        return MatchPrice
    else:
        return MatchPrice - PriorPrice

stock_list = {}

for stock in array_stocks:
    stock_values = stock.split('|')
    new_symbol = stock_values[0]
    stock_list[new_symbol] = {}
    for i in range (1, len(stock_values)):
        if len(stock_values[i]) == 0:
##            stock_values[i] = None
            stock_values[i] = ''
        else:
            stock_values[i] = float(stock_values[i])
    
    if not stock_values[1] is '':
        stock_list[new_symbol]['CeilingPrice'] = int(stock_values[1] * 1000)
    else:
        stock_list[new_symbol]['CeilingPrice'] = stock_values[1]
        
    if not stock_values[2] is '':
        stock_list[new_symbol]['FloorPrice'] = int(stock_values[2] * 1000)
    else:
        stock_list[new_symbol]['FloorPrice'] = stock_values[2]
        
    if not stock_values[3] is '':
        stock_list[new_symbol]['PriorPrice'] = int(stock_values[3] * 1000)
    else:
        stock_list[new_symbol]['PriorPrice'] = stock_values[3]
    

    if not stock_values[4] is '':
        stock_list[new_symbol]['Session1Price'] = int(stock_values[4] * 1000)
    else:
        stock_list[new_symbol]['Session1Price'] = stock_values[4]
        
    if not stock_values[5] is '':
        stock_list[new_symbol]['Session1Qtty'] = int(stock_values[5] * 10)
    else:
        stock_list[new_symbol]['Session1Qtty'] = stock_values[5]
        
    if not stock_values[6] is '':
        stock_list[new_symbol]['Session2Price'] = int(stock_values[6] * 1000)
    else:
        stock_list[new_symbol]['Session2Price'] = stock_values[6]
        
    if not stock_values[7] is '':
        stock_list[new_symbol]['Session2Qtty'] = int(stock_values[7] * 10)
    else:
        stock_list[new_symbol]['Session2Qtty'] = stock_values[7]

    if not stock_values[8] is '':
        stock_list[new_symbol]['BidP1'] = int(stock_values[8] * 1000)
    else:
        stock_list[new_symbol]['BidP1'] = stock_values[8]
        
    if not stock_values[9] is '':
        stock_list[new_symbol]['BidV1'] = int(stock_values[9] * 10)
    else:
        stock_list[new_symbol]['BidV1'] = stock_values[9]
    
    if not stock_values[10] is '':
        stock_list[new_symbol]['BidP2'] = int(stock_values[10] * 1000)
    else:
        stock_list[new_symbol]['BidP2'] = stock_values[10]
    
    if not stock_values[11] is '':
        stock_list[new_symbol]['BidV2'] = int(stock_values[11] * 10)
    else:
        stock_list[new_symbol]['BidV2'] = stock_values[11]
        
    if not stock_values[12] is '':
        stock_list[new_symbol]['BidP3'] = int(stock_values[12] * 1000)
    else:
        stock_list[new_symbol]['BidP3'] = stock_values[12]
        
    if not stock_values[13] is '':
        stock_list[new_symbol]['BidV3'] = int(stock_values[13] * 10)
    else:
        stock_list[new_symbol]['BidV3'] = stock_values[13]
    
    if not stock_values[14] is '':
        stock_list[new_symbol]['MatchPrice'] = int(stock_values[14] * 1000)
    else:
        stock_list[new_symbol]['MatchPrice'] = stock_values[14]
    
    if not stock_values[15] is '':
        stock_list[new_symbol]['MatchQtty'] = int(stock_values[15] * 10)
    else:
        stock_list[new_symbol]['MatchQtty'] = stock_values[15]
        
    if not stock_values[16] is '':
        stock_list[new_symbol]['OfferP1'] = int(stock_values[16] * 1000)
    else:
        stock_list[new_symbol]['OfferP1'] = stock_values[16]
    
    if not stock_values[17] is '':
        stock_list[new_symbol]['OfferV1'] = int(stock_values[17] * 10)
    else:
        stock_list[new_symbol]['OfferV1'] = stock_values[17]
        
    if not stock_values[18] is '':
        stock_list[new_symbol]['OfferP2'] = int(stock_values[18] * 1000)
    else:
        stock_list[new_symbol]['OfferP2'] = stock_values[18]
        
    if not stock_values[19] is '':
        stock_list[new_symbol]['OfferV2'] = int(stock_values[19] * 10)
    else:
        stock_list[new_symbol]['OfferV2'] = stock_values[19]
    
    if not stock_values[20] is '':
        stock_list[new_symbol]['OfferP3'] = int(stock_values[20] * 1000)
    else:
        stock_list[new_symbol]['OfferP3'] = stock_values[20]
        
    if not stock_values[21] is '':
        stock_list[new_symbol]['OfferV3'] = int(stock_values[21] * 10)
    else:
        stock_list[new_symbol]['OfferV3'] = stock_values[21]
        
    if not stock_values[22] is '':
        stock_list[new_symbol]['HighPrice'] = int(stock_values[22] * 1000)
    else:
        stock_list[new_symbol]['HighPrice'] = stock_values[22]
    
    if not stock_values[23] is '':
        stock_list[new_symbol]['LowPrice'] = int(stock_values[23] * 1000)
    else:
        stock_list[new_symbol]['LowPrice'] = stock_values[23]
        
    if not stock_values[24] is '':
        stock_list[new_symbol]['AvrPrice'] = int(stock_values[24] * 1000)
    else:
        stock_list[new_symbol]['AvrPrice'] = stock_values[24]
        
    if not stock_values[25] is '':
        stock_list[new_symbol]['TotalQtty'] = int(stock_values[25] * 10)
    else:
        stock_list[new_symbol]['TotalQtty'] = stock_values[25]
        
    if not stock_values[26] is '':
        stock_list[new_symbol]['FBuyQtty'] = int(stock_values[26] * 10)
    else:
        stock_list[new_symbol]['FBuyQtty'] = stock_values[26]
        
    if not stock_values[27] is '':
        stock_list[new_symbol]['FCurrentRoom'] = int(stock_values[27] * 10)
    else:
        stock_list[new_symbol]['FCurrentRoom'] = stock_values[27]
        
    if not stock_values[28] is '':
        stock_list[new_symbol]['FSellQtty'] = int(stock_values[28] * 10)
    else:
        stock_list[new_symbol]['FSellQtty'] = stock_values[28]

##with open('output.txt', 'w') as f:
##    for symbol in stock_list:
##        print (symbol, stock_list[symbol]['CeilingPrice'],
##        stock_list[symbol]['FloorPrice'], stock_list[symbol]['PriorPrice'],
##        stock_list[symbol]['Session1Price'], stock_list[symbol]['Session1Qtty'],
##        stock_list[symbol]['Session2Price'], stock_list[symbol]['Session2Qtty'],
##        stock_list[symbol]['BidV3'], stock_list[symbol]['BidP3'],
##        stock_list[symbol]['BidV2'], stock_list[symbol]['BidP2'],
##        stock_list[symbol]['BidV1'], stock_list[symbol]['BidP1'],
##        stock_list[symbol]['MatchPrice'], stock_list[symbol]['MatchQtty'],
##        Percent(stock_list[symbol]['MatchPrice'], stock_list[symbol]['PriorPrice']), \
##        stock_list[symbol]['OfferP1'], stock_list[symbol]['OfferV1'],
##        stock_list[symbol]['OfferP2'], stock_list[symbol]['OfferV2'],
##        stock_list[symbol]['OfferP3'], stock_list[symbol]['OfferV3'],
##        stock_list[symbol]['HighPrice'], stock_list[symbol]['LowPrice'],
##        stock_list[symbol]['AvrPrice'], stock_list[symbol]['TotalQtty'],
##        stock_list[symbol]['FBuyQtty'], stock_list[symbol]['FSellQtty'],
##        stock_list[symbol]['FCurrentRoom'], sep=';', file = f)

with open('output.txt', 'w') as f:
    for symbol in stock_list:
        print (symbol, stock_list[symbol]['CeilingPrice'],
        stock_list[symbol]['FloorPrice'], stock_list[symbol]['PriorPrice'],
        stock_list[symbol]['BidV3'], stock_list[symbol]['BidP3'],
        stock_list[symbol]['BidV2'], stock_list[symbol]['BidP2'],
        stock_list[symbol]['BidV1'], stock_list[symbol]['BidP1'],
        stock_list[symbol]['MatchPrice'], stock_list[symbol]['MatchQtty'],
        Percent(stock_list[symbol]['MatchPrice'], stock_list[symbol]['PriorPrice']), \
        stock_list[symbol]['OfferP1'], stock_list[symbol]['OfferV1'],
        stock_list[symbol]['OfferP2'], stock_list[symbol]['OfferV2'],
        stock_list[symbol]['OfferP3'], stock_list[symbol]['OfferV3'],
        stock_list[symbol]['HighPrice'], stock_list[symbol]['LowPrice'],
        stock_list[symbol]['AvrPrice'], stock_list[symbol]['TotalQtty'],
        stock_list[symbol]['FBuyQtty'], stock_list[symbol]['FSellQtty'],
        stock_list[symbol]['FCurrentRoom'], sep=';', file = f)
