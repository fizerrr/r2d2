import tweepy
from textblob import TextBlob
import os
from dotenv import load_dotenv
import yfinance as yf


load_dotenv()

# Ustawienia kluczy API Twittera
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Utwórz obiekt autoryzacji Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Utwórz obiekt API Tweepy
api = tweepy.API(auth)

# Zdefiniuj hasztagi i wyszukaj tweetów
hashtag = "#Apple"
public_tweets = api.search(hashtag)

# Analiza sentymentu tweetów
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)