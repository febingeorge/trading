import requests
import shutil
import csv
def callme():
	url1 = "http://real-chart.finance.yahoo.com/table.csv?s="
	url2 = ".BO&a=04&b=2&c=1995&d=07&e=10&f=2016&g=d&ignore=.csv"
	finalurl = url1+stockname+url2
	r = requests.get(finalurl, verify=False,stream=True)
	if r.status_code!=200:
		print "Failure!!"
        	exit()
    	else:
        	r.raw.decode_content = True
        	with open("file1.csv", 'wb') as f:
            		shutil.copyfileobj(r.raw, f)
        		print "Success"

if __name__ == '__main__':
   	csvfile = open('ListOfScrips.csv','rb')
	stockreader = csv.reader(csvfile);
	for row in stockreader:
		print row[1]
		break
	
	# callme()

