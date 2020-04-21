#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 06:43:27 2020

@author: amandashay
"""
# Register aaccount https://iexcloud.io/


# MCS API Token: pk_44de71531a5d400bb1bd98a2c7dd011d <- Yahoo.com
# MCS API Token: pk_470c2230657e4df083d1a54d0b1c15b5 <- google.com
# MCS API Token: pk_833e506a9b0b401a86305de47e566600 <- icloud.com

# pip install iexfinance

import pandas as pd

# Pull the list of S&P 500 Symbols 

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df.to_csv('S&P500-Info.csv')
df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])

import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True, 
                'axes.titlepad':20})

from iexfinance.stocks import get_historical_data

# Read S&P 500 Symbols from the previously created .csv file
sp = pd.read_csv('S&P500-Symbols.csv', index_col=[0])



# Getting Company Info (“company name”, “CEO”, “Sector” and “Industry”)
def getCompanyInfo(symbols):
    stock_batch = Stock(symbols,
                        token='pk_44de71531a5d400bb1bd98a2c7dd011d')
    company_info = stock_batch.get_company()
    return company_info

## Test Get first 5 stocks in the S&P 500.
 #############################################################  
sp_company_info = getCompanyInfo(sp["Symbol"][:5].tolist())


company_info_to_df = []
for company in sp_company_info:
    company_info_to_df.append(sp_company_info[company])
    
#############################################################    
    
columns = ['symbol', 'companyName', 'exchange',
           'industry', 'website', 'CEO', 'sector']
df = pd.DataFrame(company_info_to_df, columns=columns )
df.head()


## Get the earnings of a single company
def getEarnings(symbol):
    stock_batch = Stock(symbol,
                        token='pk_470c2230657e4df083d1a54d0b1c15b5')
    earnings = stock_batch.get_earnings(last=4)
    return earnings

single_stock_earnings = getEarnings(sp["Symbol"][0])

## To get the earnings of a single company in a data frame
df_earnings = pd.DataFrame(single_stock_earnings)


## Getting and Historical Prices
def getHistoricalPrices(stock):
    return get_historical_data(stock, start, end, 
                               output_format='pandas', 
                               token='pk_833e506a9b0b401a86305de47e566600')
 
start = datetime(2020, 1, 1)
end = datetime(2020, 4, 3)
single_stock_history = getHistoricalPrices(sp["Symbol"][322])
double_stock_history = getHistoricalPrices(sp["Symbol"][252])

single_stock_history['close'].plot(label="MSFT Close")
double_stock_history['close'].plot(label="INTC Close")


# Increase ticks granularity
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
single_stock_history['close'].plot(ax=subplot)
subplot.set_xlabel("2020")
subplot.set_ylabel("Price")
subplot.locator_params(nbins=40, axis='x')
fig.show()


# Rotate X ticks
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
single_stock_history[{'open','high','low','close'}].plot(ax=subplot, rot=45)
subplot.set_xlabel("2020")
subplot.set_ylabel("Price")
subplot.locator_params(nbins=40, axis='x')
fig.show()

# Add log scale
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
single_stock_history[{'open','high','low','close'}].plot(ax=subplot, rot=45, logy=True)
subplot.set_xlabel("2020")
subplot.set_ylabel("Price")
subplot.locator_params(nbins=40, axis='x')
fig.show()

# Add grid
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
single_stock_history[{'open','high','low','close'}].plot(ax=subplot, rot=45, grid=True)


subplot.set_xlabel("2020")
subplot.set_ylabel("Price")
subplot.locator_params(nbins=40, axis='x')
fig.show()


# Set fonts
title_font = {'family': 'source sans pro',
              'color': 'darkblue',
              'weight': 'normal',
              'size' :20,
              }
labels_font = {'family': 'consolas',
              'color': 'darkred',
              'weight': 'normal',
              'size' :16,
              }

fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
single_stock_history[{'open','high','low','close'}].plot(ax=subplot, rot=45, grid=True)
single_stock_history['close'].plot(ax=subplot, rot=45, grid=True)
#double_stock_history['close'].plot(ax=subplot, rot=45, grid=True)
subplot.set_xlabel("Year 2020", fontdict=labels_font, labelpad=10)
subplot.set_ylabel("Price", fontdict=labels_font)
subplot.locator_params(nbins=40, axis='x')
subplot.set_title("MSFT Historical Price", fontdict=title_font)
#subplot.set_title("MSFT vs INTC", fontdict=title_font)
fig.show()


#Save to files
fig.savefig('plot2.png')
fig.savefig('plot2.svg', format='svg')