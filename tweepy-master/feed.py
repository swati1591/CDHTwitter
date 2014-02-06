
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey='PNFPGSNhgTXwqox3aophLg'
csecret='xyMoszMJ12nzOZO1oVwEfqrjWS6Y5wc4VHwTZjHhYY'
atoken='448269244-ufxOBWhanX5VwsbO2Y5i6pw9fMooymPLqIsWiwSK'
asecret='VN6StkzkMffTcH7mPRaehVoP05YaKWMY9kbePXM2k6ztH'

class listener(StreamListener):
	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track = ["car"])
