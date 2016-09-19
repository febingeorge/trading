import urllib
import re
import csv
import timeit


def getfundamentals(stockname):
	url1 = 'https://finance.yahoo.com/quote/'
	midurl = '.BO'
	url2 = '?p='
	finalurl = url1+stockname+midurl+url2+stockname+midurl
	print finalurl
	htmlfile = urllib.urlopen(finalurl)
	htmltext = htmlfile.read()
	regex = '"trailingPE":{"raw":(.+?),"fmt"'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	if price and price[0].find('Infinity') == -1:
		price2 = float(price[0])
	else:
		price2 = 0
	regex2 = '"marketCap":{"raw":(.+?),"fmt"'
	pattern = re.compile(regex2)
	mcap = re.findall(pattern,htmltext)
	if mcap and mcap[0].find('Infinity') == -1:
		mcap2 = float(mcap[0])
	else:
		mcap2 = 0
	regex = 'averageVolume":{"raw":(.+?),"fmt"'
	pattern = re.compile(regex)
	avgvol  = re.findall(pattern,htmltext)
	if avgvol and avgvol[0].find('Infinity') == -1:
		avgvol2 = float(avgvol[0])
	else:
		avgvol2 = 0
	return (price2,mcap2,avgvol2)

if __name__ == '__main__':
	csvfile = open('ListOfScrips.csv')
	stockname = csv.reader(csvfile)
	csvwriter = csv.writer(open("fundamentals.csv",'wb'))
	header = ["stockname","PE","MCap","AvgVol"]
	csvwriter.writerow(header)
	for i,row in enumerate(stockname):
		result = getfundamentals(row[1])
		emptylist = [row[1],result[0],result[1],result[2]]
		csvwriter.writerow(emptylist)
		
	print "We are done here"
        
	#tic=timeit.default_timer()
	#pevalue= getfundamentals("ABB.BO")
	#print pevalue
	#toc=timeit.default_timer()
	#print (toc-tic)
