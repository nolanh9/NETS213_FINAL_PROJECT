import tweepy
import pandas as pd
import time 
from better_profanity import profanity
profanity.load_censor_words()

consumer_key = "go9DQzoey5FzFSc7id2JAA4tt"
consumer_secret = "Z7XvAEypJRIDS2aVg2YJ32ikM4o9wvoJg41rd6mL2RfmZs2Hyg"

access_token = "1462563144-mFEXQ1ApOSi1r7h0HwV6Wof4vLHaRhjmaz54lfe"
access_token_secert = "RgodHNMtrpSf3I6OSNLCLOIeOdln3DROKsDbDYcXEukIb"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secert)
api = tweepy.API(auth, wait_on_rate_limit=True)

users = ['@benshapiro', '@aoc', '@SamHarrisOrg', '@tedcruz', '@IlhanMN', '@NYGovCuomo', '@POTUS', '@VP', '@SenGillibrand', '@BarackObama', '@HawleyMO', '@LeaderMcConnell', '@FoxNews', '@AP', '@mtgreenee', '@michellemalkin', '@michaeljohns', '@GlennBeck', '@justinamash', '@CoryBooker', '@XavierBecerra']

all_tweets = []
for name in users:
    try:
        tweets = tweepy.Cursor(api.user_timeline, screen_name=name, tweet_mode='extended').items(400)

        tweets_list = [[profanity.censor(tweet.full_text.encode("ascii", "ignore").decode()), tweet.id] for tweet in tweets if (not 'RT' in tweet.full_text and not 'http' in tweet.full_text)]

        all_tweets.extend(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)

tweets_df = pd.DataFrame(all_tweets)
tweets_df.columns = ['tweet', 'tweet_id']
tweets_df.to_csv('tweets-clean.csv')