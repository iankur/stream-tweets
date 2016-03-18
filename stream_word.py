#!/usr/bin/python
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import re
import time

#several keys required for opening a connection
consumer_key = "9YsoGNrY7P6jdJSFNBdwxehvN"
consumer_secret = "oGD4L92pHZzrAFJcZ1qIaGNges15qMfbARhL00e3KqON13IP1D"
access_token = "708550108011364352-ZpSSKV97JGgHaBVyOhjrvcd0km1OHEY"
access_secret = "Cz7QObZJ0BREaJJtodEjR7G3Y7YaBBcWIW1SpGAMgX3JD"
dict_word = {}
time1 = time.time()	#start time
time2 = time1
N = 1000			#max size of cache
flag = 0			#flag to output every 1 minute

class MyStreamListener(StreamListener):

	def update_score(self):						#this function updates count of each word
	#	time2 = time.time()						#use time2 to update dictionary
		if len(dict_word) > 0:					#do not look into dictionary if empty
			key_dict = dict_word.keys()			#list of keys to be updated
			for word in key_dict:
				if(time2 - dict_word[word][1] >= 60):	#decrease the score of entry if older than 60 sec
					dict_word[word][0] = dict_word[word][0] - 1
					if(dict_word[word][0] < 0):			#delete entry if score < 0
						del dict_word[word]

	def process_data(self, data):				#this function processes twitter data
		global time1
		global time2
		global flag
		list_words = data.split()				#list of words in data	
		length = len(dict_word)

		for word in list_words:					#these are the words to be inserted in dictionary
			if(time.time() - time1 >= 30):
				break
			if length == N:						#if dictionary reaches its size
				key = dict_word.keys()			#list of present keys in dictionary
				for entry in key:				#delete entry with 0 score
					if(dict_word[entry][0] == 0):
						del dict_word[entry]
				length = len(dict_word)
				if(length == N):				#if size of dictionary does not reduce
					break						#then do not add any more words

			if(word in dict_word):				#if word is already present then update its score
				dict_word[word][0] = dict_word[word][0] + 1
				dict_word[word][1] = time.time() #Note time when entry is updated
			else:								#else word is new. Insert it in dictionary
				dict_word[word] = [1, time.time()]	#Note time when entry is inserted
				length = length + 1				#use this time later to determine age of entry

		if(time.time() - time1 >= 30):			#update dictionary every 30 sec
			time1 = time.time()
			time2 = time1
			flag = flag + 1
			self.update_score()
			if(len(dict_word) > 0 and flag == 2): #flag = 2 => 60 seconds passed
				for keys in dict_word:			#print words in dictionary now
					if(dict_word[keys][0] > 1):
						print dict_word[keys][0], keys
				flag = 0	#update flag to print on every 60 sec
				print 'Now hold for another 60 seconds'

	def on_data(self, raw_data):

		data = json.loads(raw_data)
		if("text" in data):				#if there is any tweet data, its key will be 'text'
			data1 = [data["text"]]		#extract tweet from tons of data
		else:							#else go for next tweet data
			return(True)

		#remove the username of person who tweeted, if any, from the extracted tweet
		#also remove the hyperlinks, if any, from the extracted tweet
		if(re.findall('^[\S \s]*@[\S]*:', data1[0])):						#check for username in the extracted data
			data1 = re.findall('^[\S \s]*@[\S]*:([\S \s]*)', data1[0])		#modified data without username
			while (re.findall('http[\S \s]*', data1[0])):					#repeat till any hyperlink remains
				m = re.search('http[\S]*', data1[0])						#start and end indices of hyperlink
				data1 = [data1[0][:m.start()] + data1[0][m.end():]]
		
		else:	#similarly remove hyperlinks when username was not there
			while (re.findall('http[\S \s]*', data1[0])):
				m = re.search('http[\S]*', data1[0])
				data1 = [data1[0][:m.start()] + data1[0][m.end():]]
				
		#process data as required
		self.process_data(data1[0])
		return(True)

	def on_error(self, status):
		print status

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

keyword = raw_input("Enter a keyword: ")

myStreanListener = MyStreamListener()
myStream = Stream(auth, myStreanListener)
myStream.filter(track=[keyword])
