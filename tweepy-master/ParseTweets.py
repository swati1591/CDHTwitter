import os 
import sys
import time



fw=open("Tokenized_tweets",'w')
def tokenize(line):
	tok=line.split(' ')
	return tok

def tweet_by_tweet():
	f=open("Collect_User_Tweets",'r')
	p=f.readlines()
	for i in p:
		x=tokenize(i.strip('\n'))
		fw.write(str(x))
		fw.write('\n')

if __name__=='__main__':
	tweet_by_tweet()
