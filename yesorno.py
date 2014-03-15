from __future__ import division
import urllib
import json as json
while True:
	yesCount = 0
	noCount = 0
	z = urllib.urlencode ({'q' : raw_input(":")})
	search = json.loads(urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + z).read())
	results = search['responseData']['results']
	result = urllib.urlopen(results[0]['url']).read()
	print(results[0]['url'])
	yes = open('yes.txt','r').read().split(',')
	no = open('no.txt','r').read().split(',')
	for a in yes:
		yesCount = yesCount + result.count(a)
	for a in no:
		noCount = noCount + result.count(a)
	if yesCount > 0 and noCount > 0:
		hist = open('history.csv', 'a')
		hist.write(str(yesCount/noCount)+",")
	avghist = open('history.csv').read().split(',')
	s = 0;
	for a in avghist: 
		if a != "": s += float(a)
	avg = s/len(avghist)
	if yesCount//len(yes) == 0 and noCount//len(no) == 0: print('i dont know')
	elif yesCount//len(yes)>noCount//len(no)*avg: print('yes')
	elif abs(yesCount//len(yes)-noCount//len(no)*avg)<=2: print('maybe')
	else: print('no')
	print str(yesCount//len(yes))+"-"+str(noCount//len(no)*avg)
