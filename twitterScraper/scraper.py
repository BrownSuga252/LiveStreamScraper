import tweepy
import re
import array
from collections import Counter

# Twitter public and private key for tweepy
consumer_key = 'KAOTwxGHxJpXUYvqlqcaDeocE'
consumer_secret = 'YH102k1kTvK6qpygYJ5lppqQfwGN9zq2IAjoYwy96UBLSbW5w8'
# Twitter auth keys for tweepy
access_token = '1077064276433661952-x5rqwuTxIinCqM3385dsZAzh3gVMXs'
access_token_secret = 'KbGeQWBWLpJkEiBeXKj2AwZw8WlMcctqVoGMNKheq6RTl'
# More Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Tweepy
api = tweepy.API(auth)
# Pulls tweets that contains "cricket live stream"
# cric_tweets = api.search('cricket live stream')

compiled = ""
# Stores just the tweets into compiled
for tweet in tweepy.Cursor(api.search, q='cricket live stream', since='2018-12-20', until='2018-12-25').items():
    compiled += " \n" + tweet.text

# Pattern for finding urls
regex = r"(https?:\/\/)(\s)?(www\.)?(\s?)(\w+\.)*([\w\-\s]+\/)*([\w-]+)\/?"
# Tells regex to find that pattern
pattern = re.compile(regex)
# Looks for that pattern in compiled
matches = pattern.finditer(compiled)
a = []
# Prints all matches in compiled out
for match in matches:
    a.append(match.group(0))

counted = Counter(a)

print(counted)
