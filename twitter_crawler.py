#Twitter Crawler Template by Cliff Makanda
import tweepy #https://github.com/tweepy/tweepy
import csv
import pandas as pd

#twitter API credentials
consumer_key = 'uZzYLJklo7eFh1JAVl3wfMxCS'
consumer_secret = 'I0KKzVNhZGB7cTKgSVIPdHgLbAZbwyugs6GGNmEH4t5RaWHSQL'
access_token = '3298766293-8G3JGTU3gzKMSnDh6BNwWkem5gzK9JnBwIzRrpj'
access_token_secret = 'jQZju6981NvUr9DCquPh8ReSvzjlYPLm0QFMwKbff7zfa'

#authorize twitter and initialize tweppy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#CVS File for tweets
csvFile = open('ua.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#WilliamsCollege ",count=10,
                           lang="en",
                           since="2016-11-28").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
