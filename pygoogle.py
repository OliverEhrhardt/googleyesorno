	

    from pygoogle import pygoogle
    import urllib
    while True:
            yesCount = 0
            noCount = 0
            z = str(raw_input(":"))
            search = pygoogle(z)
            search.pages=1
            result = urllib.urlopen(search.get_urls()[0]).read()
            print search.get_urls()[0]
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


