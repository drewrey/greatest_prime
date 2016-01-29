import config
import os
import tweepy

auth = tweepy.OAuthHandler(
    consumer_key = config.CONSUMER_KEY,
    consumer_secret = config.CONSUMER_SECRET)
auth.set_access_token(
    key = config.ACCESS_KEY,
    secret = config.ACCESS_SECRET)

api = tweepy.API(auth)

CUR_PATH = os.path.dirname(os.path.abspath(__file__))

number = open(os.path.join(CUR_PATH, 'M74207281.txt'), 'r').read().splitlines()
prime = ''.join(number)

def post_next_tweet():
    """read the location according to index, post next numbers"""
    index_path = os.path.join(CUR_PATH, 'index')

    try:
        previous_status = api.user_timeline(count=1)
        chunk = previous_status[0]._json['text']
        past, future = prime.split(chunk)
        tweet = future[0:140]
        api.update_status(tweet)
        print('status updated')

    except Exception as e:
        print('ack, we failed because!', e)

if __name__ == "__main__":
    post_next_tweet()
