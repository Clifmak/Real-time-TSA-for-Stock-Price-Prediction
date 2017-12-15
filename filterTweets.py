from nltk.corpus import stopwords
import textblob
import csv
import nltk
import pandas as pd

import re
#Process tweet for uniformity in sentiment analysis
#Method adapted from Christopher Potts Sentiment tokenizer
def preProcessing(tweet):
  tweet = tweet.lower()                                           #to lower case
  tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet) #convert link to URL
  tweet = re.sub('@[^\s]+','SOURCE',tweet)                        #change username to SOURCE                         
  tweet = re.sub('[\s]+', ' ', tweet)                             #remove extra white space
  tweet = re.sub(r'#([^\s]+)', r'\1', tweet)                      #remove '#'sign from word
  tweet = tweet.strip('\'"')                                      #remove white space on both sides
  return tweet

#Get NLTK stop words
def getStopWords():
  stopWords = set(stopwords.words('english'))                     #English Stopwords
  stopWords.add('SOURCE')                                         #Add source 
  stopWords.add('URL')                                            #Add url
  return stopWords

#Get Feature Vector
def getFeatureVector(tweet):
  featureVector = []
  sentence = tweet.split()                                          #tokenize
  for word in sentence:
    word = word.strip('\'"?,.')                                     #Remove special characters
    val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", word)                #Search alphanumeric characters
    if(word in getStopWords() or val is None):
      continue
    else:
      featureVector.append(word.lower())
  return featureVector

#Extract Features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features

tweet = "@JimChanos What Elon Musk did was simple: He made EVs sexy.Prior to that you had to compromise and get something like a Prius. But now he has the entire auto world that has figured that out and is coming up with aspirational cars. He’s fighting a different fight."
print(tweet + "\n" )
tweet = preProcessing(tweet)
featureVector = getFeatureVector(tweet)
print(featureVector)


#Adapted from NLTK Twitter Data Sentiment Analysis
tweetFrame = csv.reader(open('data1.csv', 'r'), delimiter=',')

featureList =[]
tweets = []
for row in tweetFrame :
    tweet = row[3]
    sentiment = row[1]
    processedTweet = preProcessing(tweet)
    featureVector = getFeatureVector(processedTweet)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment))
    featureList = list(set(featureList))
    training_set = nltk.classify.util.apply_features(extract_features, tweets)

    classifier = nltk.NaiveBayesClassifier.train(training_set)


initialTweet = "Bitcoin is going to make me filthy rich. I am so happy"
processedTweet = preProcessing(initialTweet)
print(classifier.classify(extract_features(getFeatureVector(processedTweet))))







  


