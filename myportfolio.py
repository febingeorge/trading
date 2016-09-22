import pandas.io.data as web
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import csv

def getvalue(stocks,numshares):
    now = datetime.datetime.now()
    start = datetime.date(2016,9,1)
    stockdata = web.DataReader(stocks, 'yahoo',start,now)
    cleandata = stockdata.ix['Adj Close']
    dataFrame = pd.DataFrame(cleandata)
    dataFrame.reset_index(inplace=True, drop=False)
    stocklist = dataFrame.as_matrix()
    for x in range(1,len(stocklist[0])):
        stocklist[:,x] *= int(numshares[x-1])
    
    dates = stocklist[:,0]
    stocklist = np.delete(stocklist,0,1)
    portfolio = stocklist.sum(axis=1)
    plt.plot(dates,portfolio)
    plt.show()




if __name__ == '__main__':
	csvfile = open('portfolio.csv')
	stockname = csv.reader(csvfile)
	stocks = []
	numshares = []
	for i,row in enumerate(stockname):
		if i == 0:
			continue
		else:
			stocks.append(row[0])
			numshares.append(row[1])
	#print stocks
	getvalue(stocks,numshares)

