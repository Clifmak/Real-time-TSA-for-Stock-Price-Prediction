
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
tweetSample = "@WSJ #Herbalife is Bill Ackman's greatest short. Will he win ?"
print(preProcessing(tweetSample))
