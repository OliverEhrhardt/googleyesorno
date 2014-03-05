from search import GoogleSearch, SearchError
import urllib
while True:
	yesCount = 0
	noCount = 0
	z = str(raw_input(":"))
	search = GoogleSearch(z)
	search.results_per_page=100
	result = search.get_results()
	search.page = 1
	url = urllib.urlopen(result[0].url.encode("utf8")).read()
	print result[0].url.encode("utf8")
	yes = open('yes.txt','r').read().split(',')
	no = open('no.txt','r').read().split(',')
	for a in yes:
		yesCount = yesCount + url.count(a)
	for a in no:
		noCount = noCount + url.count(a)
	if yesCount//len(yes) == 0 and noCount//len(no) == 0: print('i dont know')
	elif yesCount//len(yes)>noCount//len(no)*3: print('yes')
	elif abs(yesCount//len(yes)-noCount//len(no)*3)<=2: print('maybe')
	else: print('no')
	print str(yesCount//len(yes))+"-"+str(noCount//len(no)*3) 


