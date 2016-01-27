import config
import tweepy

auth = tweepy.OAuthHandler(
    consumer_key = config.CONSUMER_KEY,
    consumer_secret = config.CONSUMER_SECRET)
auth.set_access_token(
    key = config.ACCESS_KEY,
    secret = config.ACCESS_SECRET)

api = tweepy.API(auth)

number = open('M74207281.txt', 'r').read().splitlines()
prime = ''.join(number)

def post_next_tweet():
    """read the location according to index, post next numbers"""
    with open('index', 'r') as f:
        loc = f.read().splitlines()
        loc = int(loc[0])

    with open('index', 'w') as f:
        try:
            if loc == 0:
                text = prime[(loc-140):]
            else:
                text = prime[(loc-140):loc]
            api.update_status(str(text))
            f.write(str(loc+140))
        except Exception as e:
            f.write(str(loc))
            print('ack, we failed because!', e)

