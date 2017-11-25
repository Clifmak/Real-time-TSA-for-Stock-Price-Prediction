# Real-time-TSA-for-Stock-Price-Prediction

Real-time Twitter Sentiment Analysis for Stock Price Prediction


1. Overview of Problem

Our goal is to create a system for real-time analysis of Twitter public sentiment towards a basket of stocks making up the NASDAQ-1001 and predict future stock prices.  Twitter is an online news and social networking service where users post and interact with messages called “tweets”. It has become a central site were influential people and the general public express their opinions on a range of topics from politics to finance. Current events and breaking news are often closely followed by an increase in tweet volume. When prominent business people express their opinions on a stock or a company, they can generate public conversation; this often influences public opinion and can drive stock prices up or down. This presents a unique opportunity to gauge the relationship between public sentiment and stock price movement. 

According to the efficient-market hypothesis (Fama 1970), share prices reflect all publicly available information. The consensus of public opinion towards a stock is built into the price. Changes in public sentiment towards a particular stock or company is reflected by the stock price. Twitter Sentiment Analysis (TSA) provides a way to measure changes in public opinion on a stock, and predict the corresponding change in the stock price. Stock price prediction can be useful to investment managers. It can inform their decision to buy, sell or hold financial securities.

   2. Survey of Existing Work

Over the past decade, the rise of social networking sites has presented the academic community with a resource for sentiment analysis research. This has resulted in significant research and interest in mining sentiment and opinions. Twitter sentiment analysis has been used to study the relationships between the stock market and twitter mood, politics and elections (Bollen et al., 2001; Wang et al., 2012, Tusmajan et al., 2010).  For example, Bollen found a predictive correlation between measurement of public mood states from Twitter feeds and the stock market; Wang presented a system for real-time analysis of the 2012 U.S presidential elections. Previous work on Twitter Sentiment Analysis has differed in their approaches. Before 2002, most methods were partially knowledge based. (Pang et al. 2002) showed that machine learning techniques can outperform knowledge based approaches.  Fully supervised (Jansen 2009) and distantly supervised (Davidov 2010) approaches have both been used for TSA. Our approach will extend Bollen’s work and use a semi-supervised machine learning approach to mine public sentiment and predict stock prices.

3. Our Approach

Twitter Sentiment Analysis is a classification problem. Our language model will be adapted for TSA. The minimum set of classification will be negative/positive/neutral. Tweets from the same class will form one document. There will be two sets of classifications: polarity classification and subjective classification. In polarity classification, we will learn two language models: one for the positive class and another for the negative class. In subjective classification, we will learn two classes: subjective and objective. Our classifier will be a naïve Bayes model on unigram (and/or other) features. The features will include tweet volume, retweets, and  influence of Twitter user.  Our approach will focus on the daily volume of tweets, and will predict future stock prices of the NASDAQ-100. The time-window of the prediction will be determined by our evaluations of the system.
 
We will use a semi-supervised approach with data consisting of prerecorded tweets and real-time Twitter data. Tweets can contain relevant and irrelevant information such as emoticons, slang, repetitions and user mentions. We will preprocess tweet data to format it for our model. Stocks making up the NASDAQ 100 have to be matched to the relevant tweets. We will tokenize our tweets to obtain stock and/or company names.
 
Live tweet data will be mined from Twitter, and our labeled data set is the publicly available Sanders Corpus. It consists of 5513 labeled tweets collected on the topics:  Google, Apple, Microsoft and Twitter.  A “paper” portfolio of companies making up the NASDAQ-100 will be managed. Real-time stock prices data will be fetched from Yahoo Finance. Decisions on holding, buying or selling securities in our “paper” portfolio will be based on the sentimental model.
 
A visualization dashboard will show the NASDAQ-100 stocks, public sentiment, the predicted stock price, and the ‘realized’ stock price. We will also present the returns of our “paper” NASDAQ 100 portfolio relative to the NASDAQ 100 index fund.

We intend to build our system using Python. We use Twitter’s API and Yahoo Finance API.
 

 4.     Plan of Milestones
 
·      Meeting with Prof. Park.
·      Download and filter labeled Twitter data
·      Crawl Real-time Twitter Data.
·      Add throttle to pre-recorded data.
·      Preprocess Twitter Data.
·      Fetch NASDAQ 100 stock price data.
·      Match tweet data to stock or company names.
·      Create a Sentiment Model.
·      Aggregate sentiment by stock/company name.
·      Build ‘paper’ NASDAQ 100 portfolio.
·      Create a stock prediction model using sentiment data.
·      Visualization
·      Final Report Paper and Code Submission
