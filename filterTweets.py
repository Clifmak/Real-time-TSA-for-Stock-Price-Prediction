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

#tweet = "@JimChanos What Elon Musk did was simple: He made EVs sexy.Prior to that you had to compromise and get something like a Prius. But now he has the entire auto world that has figured that out and is coming up with aspirational cars. He’s fighting a different fight."
#print(tweet + "\n" )
#tweet = preProcessing(tweet)
#featureVector0 = getFeatureVector(tweet)
#print(featureVector0)


#Adapted from NLTK Twitter Data Sentiment Analysis
#tweetFrame = csv.reader(open('data4.csv', 'r'), quotechar='|', delimiter = '\t')

#featureList =[]
#tweets = []
#i = 0
#for row in tweetFrame :
#    tweety = row[2]
#    sentiment = row[1]
#    processedTweet = preProcessing(tweety)
#    featureVector1 = getFeatureVector(processedTweet)
#   featureList.extend(featureVector1)
#    tweets.append((featureVector1, sentiment))
#    featureList = list(set(featureList))
#    training_set = nltk.classify.util.apply_features(extract_features, tweets)
    #print(row[1] + " " + row[2] + "\n")
#classifier = nltk.NaiveBayesClassifier.train(training_set)
#print(classifier.labels())
    


#initialTweet = "Bitcoin is going to make me filthy rich. I am so happy"


#initialTweet = "When analysts and pundits are saying I don't see $GE outperforming in 2018, It means the selling climax is almost over and the bottom is near. Consider accumulating at this level if you have a strong stomach to handle negativity in $GE."
#processedTweet = preProcessing(initialTweet)
#blob = textblob.TextBlob(initialTweet, analyzer=textblob.sentiments.NaiveBayesAnalyzer())
#print(blob.sentiment.p_pos, blob.sentiment.p_neg)

#print(classifier.classify(extract_features(getFeatureVector(processedTweet))))

if __name__ == '__main__':
    tweetFrame = csv.reader(open('data4.csv', 'r'), quotechar='|', delimiter = '\t')

    featureList =[]
    tweets = []
    i = 0
    for row in tweetFrame :
        tweety = row[2]
        sentiment = row[1]
        processedTweet = preProcessing(tweety)
        featureVector1 = getFeatureVector(processedTweet)
        featureList.extend(featureVector1)
        tweets.append((featureVector1, sentiment))
        featureList = list(set(featureList))
        training_set = nltk.classify.util.apply_features(extract_features, tweets)
        #print(row[1] + " " + row[2] + "\n")
    
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    #initialTweet = "When analysts and pundits are saying I don't see $GE outperforming in 2018, It means the selling climax is almost over and the bottom is near. Consider accumulating at this level if you have a strong stomach to handle negativity in $GE."
    initialTweet = "$CSX so far smells like pure buyback action this morn; question is, when bb done, does it go off a cliff as sellers continue?"
    processedTweet = preProcessing(initialTweet)
    blob = textblob.TextBlob(initialTweet, analyzer=textblob.sentiments.NaiveBayesAnalyzer())
    print("Tweet:" + " " + initialTweet + "\n")
    print("Model Sentiment Value:" + " " + classifier.classify(extract_features(getFeatureVector(processedTweet))) + "\n")
    print("TextBlob Positive Sentiment Value:" + " " + blob.sentiment.p_pos)
    print("TextBlob Negative Sentiment Value:" + " " + blob.sentiment.p_neg)




  


