from nltk.corpus import stopwords


def replaceRepetition(s):
  pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
  return pattern.sub(r"\1\1", s)

def getStopWords():
  stopWords = set(stopwords.words('english'))
  stopWords.append('SOURCE')
  stopWords.append('URL')
  return stopWords

def featureVector(tweet):
  featureVector = []
  sentence = tweet.split()
  for word in sentence:
    word = replacerepetition(word)
    word = word.strip('\'"?,.')
    if(word in getStopWords() or val is None):
      continue
    else:
      featureVector.append(word.lower())
  return featureVector

tweet = "What Elon did was simple: He made EVs sexy.Prior to that you had to compromise and get something like a Prius. But now he has the entire auto world that has figured that out and is coming up with aspirational cars. He’s fighting a different fight."
      
  


