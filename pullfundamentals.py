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
    regex2 = '$MARKET_CAP.1">(.+?)</td'
    pattern = re.compile(regex2)
    mcap = re.findall(pattern,htmltext)
    mcap2 = mcap[0]
    regex = 'averageVolume":{"raw":(.+?),"fmt"'
    pattern = re.compile(regex)
    avgvol  = re.findall(pattern,htmltext)
    avgvol2 = float(price[0])
	return (price2,mcap2,avgvol2)

if __name__ == '__main__':
	csvfile = open('ListOfScrips.csv')
	stockname = csv.reader(csvfile)
	csvwriter = csv.writer(open("fundamentals.csv",'wb'))
	for i,row in enumerate(stockname):
        	if i == 3:
			break
        result = getfundamentals(row[1])
		emptylist = [row[1],,result[1],result[2],result[3]]
		csvwriter.writerow(emptylist)
        
	#tic=timeit.default_timer()
	#pevalue= getfundamentals("ABB.BO")
	#print pevalue
	#toc=timeit.default_timer()
	#print (toc-tic)
