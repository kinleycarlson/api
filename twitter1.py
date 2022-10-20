import keys
import tweepy
import json

#from tweetutilities import print_tweets

auth = tweepy.OAuthHandler(keys.api_key, keys.api_key_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print('Success')
except:
    print('Failed')

keywords = 'kanyewest'
result_type = 'popular'


tweets = api.search_tweets(keywords,lang = 'en',result_type = result_type, count = 10)

#print(tweets)

for tweet in tweets:
    print(tweet.user.screen_name, ":", tweet.text, "\n\n")
    input()

