# Twitter API Crawler
# -*- coding: utf-8 -*-

'''
Author: chengjun wang
Email: wangchj04@gmail.com
Hong Kong, 2013/01/20
'''
import sys
import tweepy
import codecs
import time
from time import clock
import klout
from klout import *
import twython
from twython import Twython

'''OAuth Authentication'''
consumer_key="PNFPGSNhgTXwqox3aophLg"
consumer_secret="xyMoszMJ12nzOZO1oVwEfqrjWS6Y5wc4VHwTZjHhYY"
access_token="448269244-ufxOBWhanX5VwsbO2Y5i6pw9fMooymPLqIsWiwSK"
access_token_secret="VN6StkzkMffTcH7mPRaehVoP05YaKWMY9kbePXM2k6ztH"

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth1)
twitter =Twython(consumer_key, consumer_secret,access_token, access_token_secret)

'''
# Note: Had you wanted to perform the full OAuth dance instead of using
# an access key and access secret, you could have uses the following
# four lines of code instead of the previous line that manually set the
# access token via auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET).
# auth_url = auth.get_authorization_url(signin_with_twitter=True)
# webbrowser.open(auth_url)
# verifier = raw_input('PIN: ').strip()
# auth.get_access_token(verifier)
'''

#file = open("tweets.csv",'wb') # save to csv file

print api.me().name # api.update_status('Updating using OAuth authentication via Tweepy!')

start = clock()
print start

'''Specify the stream'''
class StreamListenerChengjun(tweepy.StreamListener):
	def on_status(self, status):
		try:
			#tweet = status.text.encode('utf-8')
			tweet=status.text
			tweet = tweet.replace('\n', '\\n')
			#user = status.author.screen_name.encode('utf-8')
			user = status.author.screen_name
			userid = status.author.id
			time_at = status.created_at
			source = status.source
			tweetid = status.id
			timePass = clock()-start
			if timePass%60==0:
				print "I have been working for", timePass, "seconds."
			if not ('RT @' in tweet) :	# Exclude re-tweets
				print  "%s,%s,%s,%s,|%s|,%s" % (userid, user, time, tweetid, tweet, source)
			f= open('IndexUsers','a')
			#klout 

			# Make the Klout object
			k = Klout('epvjtgvg53rqz5pg5jwjz45b')
			# Get kloutId of the user by inputting a twitter screenName
    			kloutId = k.identity.klout(screenName=user).get('id')
			# Get klout score of the user
    			score = k.user.score(kloutId=kloutId).get('score')
    			print "User's klout score is: %s" % (score)
			s=twitter.show_user(screen_name=user)
			followers=s["followers_count"]
			print followers 
			#follower=tweepy.api.followers(userid)
			#u=tweepy.api.get_user(userid)
			#print u
			#print u.followers_count
			#print len(follower)
			if score>30 and followers>100:
				print 'Index User'
				f.write(user + '\t')
				f.write(str(score) + '\t')
				f.write(str(followers) + '\t')
				f.write('\n')
				print "hello"
			time.sleep(10)
			# By default all communication is not secure (HTTP). An optional secure parameter
			# can be sepcified for secure (HTTPS) communication
			k = Klout('epvjtgvg53rqz5pg5jwjz45b', secure=True)

			# Optionally a timeout parameter (seconds) can also be sent with all calls
			score = k.user.score(kloutId=kloutId, timeout=5).get('score')
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

'''Link the tube with tweet stream'''
streamTube = tweepy.Stream(auth=auth1, listener=StreamListenerChengjun(), timeout= 300)  # https://github.com/tweepy/tweepy/issues/83 # setTerms = ['good', 'goodbye', 'goodnight', 'good morning'] # streamer.filter(track = setTerms)
streamTube.sample()

file.close()
pass

timePass = time.clock()-start
print timePass

