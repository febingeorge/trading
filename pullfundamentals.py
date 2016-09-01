import urllib
import re
import csv
import timeit


def getfundamentals(stockname):
	return 0
	url1 = 'https://finance.yahoo.com/quote/'
	url2 = '/?p='
	finalurl = url1+stockname+url2+stockname
	print finalurl
	htmlfile = urllib.urlopen(finalurl)
	htmltext = htmlfile.read()
	regex = '"trailingPE":{"raw":(.+?),"fmt"'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	price2 = float(price[0])
	return price2

if __name__ == '__main__':
	csvfile = open('ListOfScrips.csv')
	stockname = csv.reader(csvfile)
	csvwriter = csv.writer(open("fundamentals.csv",'wb'))
	for i,row in enumerate(stockname):
        	if i == 3:
			break
		emptylist = [row[1],getfundamentals(row[1])]
		csvwriter.writerow(emptylist)
        
	#tic=timeit.default_timer()
	#pevalue= getfundamentals("ABB.BO")
	#print pevalue
	#toc=timeit.default_timer()
	#print (toc-tic)
