from bs4 import BeautifulSoup
import urllib2
import csv

def gethistoricaleps(stockname):
	url1 = 'http://www.bseindia.com/stock-share-price/stockreach_financials.aspx?scripcode='
	url2 = '&expandable=0'
	finalurl = url1+stockname+url2
	html = urllib2.urlopen(finalurl).read()
	soup=BeautifulSoup(html)
	table = soup.find('table',{'id' :'acr'})
	tr = table.find('td', text='EPS').parent
	td = tr.find_all('td')
	eps2016 = td[1].get_text()
	eps2015 = td[2].get_text()
	eps2014 = td[3].get_text()
	eps2013 = td[4].get_text()
	eps2012 = td[5].get_text()
	
	return (eps2016,eps2015,eps2014,eps2013,eps2012)


if __name__ == '__main__':
	csvfile = open('finalsetwithcode.csv','rb')
	stockname = csv.reader(csvfile);
	csvwriter = csv.writer(open("historicalpe.csv",'wb'))
	header = ["stockname","2016","2015","2014","2013","2012"]
	csvwriter.writerow(header)
	for i,row in enumerate(stockname):
		if i < 166:
			continue
		else:
			result = gethistoricaleps(row[1])
			emptylist = [row[0],result[0],result[1],result[2],result[3],result[4]]
			csvwriter.writerow(emptylist)
			
	print "We are done here"

