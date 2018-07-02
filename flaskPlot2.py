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

    # 5M,  15M, 30M,  2H,   4H,        1D
    # 300, 900, 1800, 7200, 14400, and 86400
    # ---------------------------------------------
    # BUY --------  price: 6200 btc: 0.01 total: 62
    # SELL -------  price: 6300 btc: 0.01 total: 63
    # fee --------    

def predict1_btc(moment, listopen, lastopen, listearn):
    if len(listopen) > 1:
        print("last open value:")
        last_open =  lastopen[-1]
        print(last_open)
        if float(moment < last_open):
            print("---- v level 1 *")
            if len(listopen) > 2:
                last_open2 = lastopen[-2]    
                if float(moment < last_open2):
                    print("---- vv level 2 **")
                    if len(listopen) > 3:
                        last_open3 = lastopen[-3]    
                        if float(moment < last_open3):
                            listearn.append(moment)
                            print("---- vvv level 3 ***")
                            print(" ============================================================== ")
                            print(" =======================J=A=C=K=P=O=T ========================= ")
                            print(" ============================================================== ")
                            print(" =============================* =============================== ")
                            print(" ==========================*=====* ============================ ")
                            print(" =======================*===========* ========================= ")
                            print(" =============*********===============********** ============== ")
                            print(" ===============*============================* ================ ")
                            print(" =================*========================* ================== ")
                            print(" ===================*=========* =========* ==================== ")
                            print(" =================*=====* ==========*======* ================== ")
                            print(" ===============*===* ===================*===* ================ ")
                            print(" =============* ===============================* ============== ")
                            print(" ====================== Prediction 100% ======================= ")
                            print(" =================== YOU EARNED BITCOINS :) =================== ")




def operacao(valorusdt, volat, lastOpPriceBtc, saldoBTC, saldoUSDT):
    if float(valorusdt) < float(lastOpPriceBtc - volat):
        print("=============================")
        print("operacao ganhar BTC na queda")
        
        print("=============================")
    if float(valorusdt) > float(lastOpPriceBtc + volat):
        print("=============================")
        print("operacao ganhar USDT na alta")
        print("=============================")


    



def read_polo1():
    '''
    print("== PYTHON DATA SCIENCE ==")
    print("=========================")
    mongo = MongoClient()
    mongo = MongoClient('mongodb://127.0.0.1:27017')
    db_cadastro = mongo['cadastro_db']
    newUser = mongo.db.db_cadastro
    registro = mongo.db.db_cadastro.find()
    '''
    print("=========================")
    # 5M,  15M, 30M,  2H,   4H,        1D
    # 300, 900, 1800, 7200, 14400, and 86400
    r = http.request('GET', 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1527595200&end=9999999999&period=300')
    myData = json.loads(r.data.decode('utf-8'))
    print(myData)
    print("== PYTHON DATA SCIENCE ==")
    print("=== POLONIEX EXCHANGE ===")
    print("")
    list_open = []
    list_close = []
    list_volume = []
    list_quoteVolume = []
    list_opens_trend = []
    list_close_trend = []
    list_earn_bitcoins = []
    list_btc = [0.01]
    list_usdt = [100]
    last_op_btc_price = [7400]
    list_op_btc = []
    list_op_usdt = []
    ct = 0
    for ls in myData:
        if myData[ct]['close']:
            momentValue = myData[ct]['close']    
            print("")
            print("value close: " + str(momentValue))
            list_close.append(momentValue)        
            #predict1_btc(momentValue, list_open, list_open, list_earn_bitcoins)
            operacao(momentValue, 200, last_op_btc_price[0], list_btc[0], list_usdt[0])

        if myData[ct]['open']:
            momentValue = myData[ct]['open']    
            print("")
            print("value open: " + str(momentValue))
            print("")
            list_open.append(momentValue)
            operacao(momentValue, 200, last_op_btc_price[0], list_btc[0], list_usdt[0])

        if myData[ct]['volume']:
            momentValue = myData[ct]['volume']    
            print("")
            print("value volume: " + str(momentValue))
            print("")
            list_volume.append(momentValue)
        if myData[ct]['quoteVolume']:
            momentValue = myData[ct]['quoteVolume']    
            print("")
            print("value quoteVolume: " + str(momentValue))
            print("")
            list_quoteVolume.append(momentValue)
        ct += 1
    

    plt.plot(list_open)
    plt.plot(list_close)
    plt.plot(list_quoteVolume)
    plt.plot(list_earn_bitcoins)
    plt.grid()
    plt.legend(['open', 'close', 'quote Volume', 'You earn bitcoins'])
    #plt.plot(list_open, list_close, 'o')
    plt.show()




read_polo1()



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



def ver_rent():
    vol1 = 100
    vol2 = 200
    vol3 = 300
    vol4 = 400
    vol5 = 500
    last_op_btc = []
    last_op_usdt = []
    myBTC = [0.01]
    myUSDT = [6300]
    # 5M,  15M, 30M,  2H,   4H,        1D
    # 300, 900, 1800, 7200, 14400, and 86400
    r = http.request('GET', 'https://poloniex.com/public?command=returnTicker')
    myData = json.loads(r.data.decode('utf-8'))
    print("== PYTHON DATA SCIENCE ==")
    print("=== POLONIEX EXCHANGE ===")
    print("")
    print(myData['USDT_BTC'])
    print("")
    btc_last = myData['USDT_BTC']['last']
    print(btc_last)
    

#ver_rent()
