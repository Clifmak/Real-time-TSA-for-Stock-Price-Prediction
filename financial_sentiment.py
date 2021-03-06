from nltk.corpus import stopwords
import textblob
import csv
import nltk
import pandas as pd
import sys

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

#tweet = "@JimChanos What Elon Musk did was simple: He made EVs sexy.Prior to that you had to compromise and get something like a Prius. But now he has the entire auto world that has figured that out and is coming up with aspirational cars. He’s fighting a different fight."
#print(tweet + "\n" )
#tweet = preProcessing(tweet)
#featureVector0 = getFeatureVector(tweet)
#print(featureVector0)



#print(classifier.classify(extract_features(getFeatureVector(processedTweet))))

#Build Sentiment Model, and Compare it to an off the shelf classifier
if __name__ == '__main__':
    #Fetch Training Dataset
    tweetFrame = csv.reader(open('data4.csv', 'r'), quotechar='|', delimiter = '\t')

    featureList =[]        #Feature Set
    tweets = []            #Tweets
    #for every row in dataset
    for row in tweetFrame :
        tweety = row[2]                                    #Get tweet
        sentiment = row[1]                                 #Get Sentiment
        processedTweet = preProcessing(tweety)             #Preprocess tweet text
        featureVector1 = getFeatureVector(processedTweet)  #Get FeatureVector
        featureList.extend(featureVector1)                 #Expand FeatureList
        tweets.append((featureVector1, sentiment))         #update tweetList
        featureList = list(set(featureList))               #Remove Duplicates
        training_set = nltk.classify.util.apply_features(extract_features, tweets)   #Extract feature vector for all tweets
        
    
    classifier = nltk.NaiveBayesClassifier.train(training_set)  #Train classifier
    #print(sys.argv)
    initialTweet = str(sys.argv[1])      
    processedTweet = preProcessing(initialTweet)
    blob = textblob.TextBlob(initialTweet, analyzer=textblob.sentiments.NaiveBayesAnalyzer())
    print("Tweet:" + " " + initialTweet + "\n")
    print("Model Sentiment Value:" + " " + classifier.classify(extract_features(getFeatureVector(processedTweet))) + "\n")
    print("TextBlob Positive Sentiment Value:" + " " + str(blob.sentiment.p_pos) + "\n")
    print("TextBlob Negative Sentiment Value:" + " " + str(blob.sentiment.p_neg))




  


