# -*- coding: utf-8 -*-
"""
Spyder Editor
host='ec2-107-20-189-29.compute-1.amazonaws.com'
This is a temporary script file.
"""


import psycopg2
conn_string = "host='localhost' dbname='lard_development' user='macbookpro' password=''"
conn = psycopg2.connect(conn_string)
conn.close()


                                                      import numpy as np
import pandas as pd
import pandas.io.data as web

#goog = web.DataReader('BABA', data_source = 'google', start = '1/1/2016', end = '5/6/2016')

#print goog.tail()

import xlrd
import pymongo

# Establish MongoDB connection
from pymongo import MongoClient
client = MongoClient()
db = client.finapp_development
collection = db['stock']
stocks = db.stocks


# open the workbook and define the worksheet
book = xlrd.open_workbook('Yahoo Ticker Symbols - Jan 2016.xlsx')
sheet = book.sheet_by_name('Stock')

new_stocks = []
# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(4, sheet.nrows):
      ticker      = sheet.cell(r,0).value
      company = sheet.cell(r,1).value
      exchange          = sheet.cell(r,2).value
      country     = sheet.cell(r,3).value
      category_name       = sheet.cell(r,4).value
      category_code = sheet.cell(r,5).value
      

      # Assign values from each row
      #values = (symbol, company, exchange, country, category_name, category_code)
      new_stocks.append({'ticker': ticker, 'company':company, 'exchange':exchange, 'country':country, 'category_name':category_name, 'category_code':category_name })

result = stocks.insert_many(new_stocks)

#print result.inserted_ids

'''
from yahoo_finance import YFinanceDataExtr
data_ext = YFinanceDataExtr()
## read  data from .csv file -- full list of stocks
csv_fname = r'~\yahoo_finance_data_extract\stocklist.csv'
stock_list = pd.read_csv(csv_fname)
# convert from pandas dataframe object to list
stock_list = list(stock_list['SYMBOL'])
#stock_list = ['S58.SI','S68.SI']
print data_ext.get_cur_quotes_fr_list(stock_list)
'''

'''
#import pymongo
from pymongo import MongoClient
client = Mongo.client()
db = client.finapp_development
collection = db['stock']
'''
