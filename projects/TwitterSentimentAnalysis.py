'''
Dependencies:
pip install tweepy
pip install -U textblob
'''

import tweepy
from textblob import TextBlob

# Authenticate
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Retrieve Tweets
public_tweets = api.search('India')


for tweet in public_tweets:
    print(tweet.text)
    
    #Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")