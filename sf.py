#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:37:05 2020

@author: amandashay
"""


import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True, 
                'axes.titlepad':20})
# Gets the version
ctx = snowflake.connector.connect(
                user='ms4446',
                password='xxxxxx',
                account='jqa18325.us-east-1',
                #warehouse='COMPUTE_WH',
                database='CITIBIKE',
                schema='public'
                )

# Create a cursor object.
cur = ctx.cursor()

    
sql = """select monthname(starttime) as "Month",
    count(*) as "Trips"
from trips
group by 1 order by 2 desc;;"""

cur.execute(sql)

df = cur.fetch_pandas_all()



# Add grid
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
df.plot.bar( x='Month', y='Trips',rot=45,  grid=True, legend=True,
            title ='Citi Bike Trips', 
            fontsize=12)
fig.show()


#Save to files
fig.savefig('plot.png')
fig.savefig('plot.svg', format='svg')


