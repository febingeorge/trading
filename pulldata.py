import requests
import shutil
import csv
import pandas.io.data as web
import pandas as pd
def callme(stockname):

	stockdata = web.DataReader(stockname, 'yahoo','2000-1-1','2016-9-11')
	cleandata = stockdata.ix['Adj Close']
	dataFrame = pd.DataFrame(cleandata)
	dataFrame.reset_index(inplace=True, drop=False)

	dataFrame.to_csv('stockdata.csv')


if __name__ == '__main__':
	csvfile = open('finalset.csv','rb')
	stockreader = csv.reader(csvfile);
	stocks = []
	#csvwriter = csv.writer(open("stockdata.csv", 'wb'))
	for i,row in enumerate(stockreader):
		if i == 0:
			continue
		#elif (i > 4):
		#	break
		else:
			stocks.append(row[0]+".BO")

	callme(stocks)


