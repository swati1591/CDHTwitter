import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

keyword='swati1591'
startingLink = 'https://twitter.com/search/realtime?q='

def main():
	try:
		sourceCode=opener.open('https://twitter.com/search/realtime?q='+keyword+'&src=hash').read()
		#print sourceCode
		splitSource = re.findall(r'<p class="js-tweet-text tweet-text">(.*?)</p>', sourceCode)
		for item in splitSource:
			#print item
			print ('-------------------')
			print re.sub(r'<.*?>', '', item)
			#time.sleep(555)
	except Exception, e:
		print str(e)
		print ' errored in the main try'
		time.sleep(555)

main()
