#Twitter Crawler Template by Cliff Makanda
import tweepy
import csv
import pandas as pd

#Credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#Authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#CVS File for tweets
csvFile = open('ua.csv', 'a')
csvWriter = csv.writer(csvFile)
