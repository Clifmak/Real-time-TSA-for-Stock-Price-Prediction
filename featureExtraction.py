#Adapted from NLTK Twitter Data Sentiment Analysis
tweetFrame = csv.reader('Sentiment Analysis Dataset.csv', 'rb')
tweets = []
for row in tweetFrame :
  sentiment = row[0]
  tweet = row[1]
  processedTweet = preprocessing
  
  
