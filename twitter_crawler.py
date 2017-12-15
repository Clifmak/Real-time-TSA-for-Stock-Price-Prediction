#Twitter Crawler Template by Cliff Makanda
import tweepy #https://github.com/tweepy/tweepy
import csv
import pandas as pd
import textblob
# https://textblob.readthedocs.io/en/dev/advanced_usage.html#sentiment-analyzers
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

'''
for tweet in tweepy.Cursor(api.search,q="#NVDA",count=10,
                               lang="en",
                               since="2016-11-28").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
'''

companyList = ["#ADP", "#ADBE", "#MSFT", "#TSLA"]
for company in companyList :
  
    neg_score = 0
    pos_score = 0
    for tweet in tweepy.Cursor(api.search,q="#"+company, sceen_name = name,
                               lang="en",
                               since="2017-11-28").items(10):
        blob = textblob.TextBlob(tweet.text, analyzer=textblob.sentiments.NaiveBayesAnalyzer())
        neg_score += blob.sentiment.p_neg
        pos_score += blob.sentiment.p_pos
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        neg_avg = neg_score/10
        pos_avg = pos_score/10
        if (neg_avg > pos_avg):
            sent = "negative"
            diff = neg_avg-pos_avg
        elif (pos_avg > neg_avg):
            sent = "positive"
            diff = pos_avg-neg_avg
        else:
            sent = "neutral"
            diff = 0
        print (company, sent, diff)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
