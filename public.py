import tweepy
import time

FILE_NAME = 'last_seen.txt'
PUMP_THIS_COIN = 'StormX'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

# API KEYS GOES HERE
# KEYS MUST BE STRINGS
'''consumer_secret =
consumer_key =
key =
secret =
'''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

tweets = api.search(PUMP_THIS_COIN,
                    since_id=read_last_seen(FILE_NAME),
                    result_type='recent')

for tweet in reversed(tweets):
    try:
        print(tweet.id_str + ' - ' + str(tweet.text))
        # api.retweet(tweet.id)
    except UnicodeEncodeError:
        print('UnicodeEncodeError')

    store_last_seen(FILE_NAME, tweet.id)

time.sleep(120)
print('Done')
