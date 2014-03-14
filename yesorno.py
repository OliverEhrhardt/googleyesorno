import urllib
import json as m_json
while True:
	yesCount = 0
	noCount = 0
	z = urllib.urlencode ({'q' : raw_input(":")})
	search = m_json.loads(urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + z).read())
	results = search['responseData']['results']
	result = urllib.urlopen(results[0]['url']).read()
	print(results[0]['url'])
	yes = open('yes.txt','r').read().split(',')
	no = open('no.txt','r').read().split(',')
	for a in yes:
		yesCount = yesCount + result.count(a)
	for a in no:
		noCount = noCount + result.count(a)
	if yesCount//len(yes) == 0 and noCount//len(no) == 0: print('i dont know')
	elif yesCount//len(yes)>noCount//len(no)*3: print('yes')
	elif abs(yesCount//len(yes)-noCount//len(no)*3)<=2: print('maybe')
	else: print('no')
	print str(yesCount//len(yes))+"-"+str(noCount//len(no)*3)
