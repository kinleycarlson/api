from cgi import print_arguments
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

'''
keywords = 'kanyewest'
result_type = 'popular'


tweets = api.search_tweets(keywords,lang = 'en',result_type = result_type, count = 10)

#print(tweets)

for tweet in tweets:
    print(tweet.user.screen_name, ":", tweet.text, "\n\n")
    input()

query = '#collegefootball'
result_type = 'recent'
tweets = api.search_tweets(query, lang = 'en', result_type = result_type, count = 10)

for tweet in tweets:
    print(tweet.user.screen_name, ":", tweet.text, "\n\n")
    input()

'''

NewYork = 2459115
Dallas = 2388929
Waco = 2512937
World = 1

trends_avaliable = api.get_place_trends(id= World)
#print(trends_avaliable)

outfile = open('trends.json','w')
json.dump(trends_avaliable,outfile,indent = 5)

trends_list = trends_avaliable[0]['trends']


# want only the tweets with tweet volume that is not  null
trends_list = [t for t in trends_list if t['tweet_volume']]

#number of those trends above 10,000
print(len(trends_list))

print(trends_list)

from operator import itemgetter

#sort by item in list in desc order
trends_list.sort(key = itemgetter('tweet_volume'), reverse = True)



#top 10 trending topic NYC and make word cloud 

topics = {}

for trend in trends_list:
    topics[trend['name']]= trend['tweet_volume']

from wordcloud import WordCloud

wordcloud = WordCloud(
    width = 1600, 
    height = 900,
    prefer_horizontal = 0.5,
    min_font_size = 10,
    colormap = 'prism',
    background_color = 'white'
)

wordcloud = wordcloud.fit_words(topics)

wordcloud =  wordcloud.to_file('TrendingTopics.png')
