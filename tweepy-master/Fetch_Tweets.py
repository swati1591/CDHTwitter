import sys
import os
import tweepy
import codecs
import time
from time import clock
import klout
from klout import *
import twython
from twython import Twython



consumer_key="PNFPGSNhgTXwqox3aophLg"
consumer_secret="xyMoszMJ12nzOZO1oVwEfqrjWS6Y5wc4VHwTZjHhYY"
access_token="448269244-ufxOBWhanX5VwsbO2Y5i6pw9fMooymPLqIsWiwSK"
access_token_secret="VN6StkzkMffTcH7mPRaehVoP05YaKWMY9kbePXM2k6ztH"

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth1)
twitter =Twython(consumer_key, consumer_secret,access_token, access_token_secret)	
#class FetchUserTweets(tweepy.StreamListener):
f=open("Index_user_handles",'r')
users=f.readlines()
fw=open("Collect_User_Tweets",'w')
	
def pass_user():
	for u in users:
		fetch(u)
		time.sleep(5)
def fetch(users):
	try:
		#code for fetching tweets of user
		#tweet=api.user_timeline(screen_name=users, include_rts=False, count=50)
		tweet=api.user_timeline(screen_name=users,count=50)
		print len(list(tweet))
		for i in tweet:
			print users
			if not ('RT @' in i.text) :
				print i.text.encode('utf-8')
				time.sleep(5)
				fw.write(i.text)
				fw.write('\n')
	except Exception, e:
        	print >> sys.stderr, 'Encountered Exception:', e
                pass
	def on_error(self, status_code):
		print 'Error: ' + repr(status_code)
                return True # False to stop
	'''def on_delete(self, status_id, user_id):
                """Called when a delete notice arrives for a status"""
                print "Delete notice for %s. %s" % (status_id, user_id)
                return'''
        def on_limit(self, track):
                """Called when a limitation notice arrvies"""
                print "!!! Limitation notice received: %s" % str(track)
                return
        def on_timeout(self):
                print >> sys.stderr, 'Timeout...'
                time.sleep(10)
                return True


#streamTube = tweepy.Stream(auth=auth1, listener=FetchUserTweets(), timeout= 300)
if __name__=='__main__':
	pass_user()	
