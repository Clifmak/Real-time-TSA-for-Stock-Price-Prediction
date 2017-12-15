from nltk.corpus import stopwords
import textblob

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


def replaceRepetition(s):
  pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
  return pattern.sub(r"\1\1", s)

def getStopWords():
  stopWords = set(stopwords.words('english'))
  stopWords.add('SOURCE')
  stopWords.add('URL')
  return stopWords

def getFeatureVector(tweet):
  featureVector = []
  sentence = tweet.split()
  for word in sentence:
    word = replaceRepetition(word)
    word = word.strip('\'"?,.')
    val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", word)
    if(word in getStopWords() or val is None):
      continue
    else:
      featureVector.append(word.lower())
  return featureVector

tweet = "@JimChanos What Elon did was simple: He made EVs sexy.Prior to that you had to compromise and get something like a Prius. But now he has the entire auto world that has figured that out and is coming up with aspirational cars. He’s fighting a different fight."
print(tweet + "\n" )
tweet = preProcessing(tweet)
featureVector = getFeatureVector(tweet)
print(featureVector)






  


