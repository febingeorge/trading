import requests
import shutil
import csv
import pandas as pd
def callme(stockname):
	url1 = "http://real-chart.finance.yahoo.com/table.csv?s="
	url2 = ".BO&a=04&b=2&c=2000&d=07&e=10&f=2016&g=d&ignore=.csv"
	finalurl = url1+stockname+url2
	r = requests.get(finalurl, verify=False,stream=True)
	if r.status_code!=200:
		print "Failure!!", stockname
		exit()
	else:
		r.raw.decode_content = True
		with open("file1.csv", 'wb') as f:
			shutil.copyfileobj(r.raw, f)
			check = pd.read_csv("file1.csv",usecols=[0, 1])
			check.to_csv("newfile.csv",mode = 'a',header=False)
		print "Success"

if __name__ == '__main__':
	csvfile = open('finalset.csv','rb')
	stockreader = csv.reader(csvfile);
	for i,row in enumerate(stockreader):
		if i == 0:
			continue
		elif (i > 4):
			break
		else:
			callme(row[0])
	#	break

	#callme("ABB")

