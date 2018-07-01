import urllib3
import urllib.parse
import urllib.request
from io import StringIO, BytesIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import urllib3
import json 
import sys, locale
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pnd 
import pymongo 
from pymongo import MongoClient 

http = urllib3.PoolManager()



def read_polo1():  
    print("== PYTHON DATA SCIENCE ==")
    print("=========================")
    mongo = MongoClient()
    mongo = MongoClient('mongodb://127.0.0.1:27017')
    db_cadastro = mongo['cadastro_db']
    newUser = mongo.db.db_cadastro
    registro = mongo.db.db_cadastro.find()
    print("=========================")
    # 5M,  15M, 30M,  2H,   4H,        1D
    # 300, 900, 1800, 7200, 14400, and 86400
    r = http.request('GET', 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1527595200&end=9999999999&period=300')
    myData = json.loads(r.data.decode('utf-8'))
    print(json.loads(r.data.decode('utf-8')))
    print("== PYTHON DATA SCIENCE ==")
    print("=== POLONIEX EXCHANGE ===")
    print("")
    list_open = []
    list_close = []
    ct = 0
    for ls in myData:
        if myData[ct]['close']:
            momentValue = myData[ct]['close']    
            print("")
            print("value close: " + str(momentValue))
            print("")
            list_close.append(momentValue)
                
        if myData[ct]['open']:
            momentValue = myData[ct]['open']    
            print("")
            print("value open: " + str(momentValue))
            print("")
            list_open.append(momentValue)

        ct += 1

    plt.plot(list_open)
    plt.plot(list_close)
    plt.grid()
    plt.legend(['open', 'close'])
    #plt.plot(list_open, list_close, 'o')
    plt.show()
    for reg in registro:
        print("- Tradex -")
        print(reg['nome'])
        if reg['nome']:
            nomeUsuario = reg['nome']
            print("***********************************")
            print("***********************************")
            print("***********************************")
            print("usuario: " + nomeUsuario)



#read_polo1()



def plot():    
    plt.style.use('fivethirtyeight')
    x = np.linspace(0, 10)
    # Fixing random state for reproducibility
    np.random.seed(19680801)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x) + x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + np.random.randn(50))
    ax.set_title("'fivethirtyeight' style sheet")
    plt.show()

#plot()