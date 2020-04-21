#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:57:57 2020

@author: Mark Shay
"""

import pandas as pd
import os

# Where our data lives
CSV_PATH = os.path.join('/Users/amandashay/Documents/corepy','artwork_data.csv')

# Read just 5 rows to see what's there
df = pd.read_csv(CSV_PATH, nrows=5)

#Specify an Index
df = pd.read_csv(CSV_PATH, nrows=5, 
                 index_col='id')

#Limit Coluumns
df = pd.read_csv(CSV_PATH, nrows=5, 
                 index_col='id',
                 usecols=['id','artist'])
# All colums that we need
COLS_TO_USE = ['id', 'artist',
               'title','medium','year',
               'acquisitionYear','height',
               'width','units']
df = pd.read_csv(CSV_PATH, 
                 usecols=COLS_TO_USE,
                 index_col='id')

# Save for later
df.to_pickle(os.path.join('/Users/amandashay/Documents/corepy','data_frame.pickle'))
