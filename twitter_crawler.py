#Twitter Crawler Template by Cliff Makanda
import tweepy #https://github.com/tweepy/tweepy
import csv
import pandas as pd

#twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#authorize twitter and initialize tweppy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#CVS File for tweets
csvFile = open('ua.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#AMZN",count=100,
                           lang="en",
                           since=datetime.datetime.today().strftime('%Y-%m-%d')).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
