def number_of_verfied_users(tweets):
    verified = 0
    n_tweets = 0
    for tweet in tweets:
        n_tweets+=1
        if tweet.user.verified:
            verified+=1

    percent_verified = (verified / n_tweets)*100

    return percent_verified, n_tweets

def count_non_ascii(tweet):
    try:
        tweet_txt = tweet.extended_tweet['full_text']
    except AttributeError:
        tweet_txt = tweet.text

    spl_tweet = tweet_txt.split()

    n_non_ascii = 0
    for w in spl_tweet:
        if not w.isascii():
            n_non_ascii+=1

    return n_non_ascii

def count_hashtags(tweet):
    try:
        tweet_txt = tweet.extended_tweet['full_text']
    except AttributeError:
        tweet_txt = tweet.text

    spl_tweet = tweet_txt.split()

    n_hashtags = 0
    for w in spl_tweet:
        if w[0] == "#":
            n_hashtags+=1

    return n_hashtags

def print_tweet(tweet):

    print("Tweet from user: ", tweet.user.name)
    print("With user ID: ", tweet.user.id_str)
    print("Number of friends: ", tweet.user.friends_count)

    if tweet.user.verified:
        print("User is verified")
    else:
        print("User is not verfied")

    print("Tweet ID: ", tweet.id)
    try:
        print(tweet.extended_tweet['full_text'])
    except AttributeError:
        print(tweet.text)
    print("--------------------------")

# API KEYS GOES HERE
# consumer_key = 'key_as_string'
# consumer_secret = 'key_as_string'
# key = 'key_as_string'
# secret = 'key_as_string'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

environment_dev = "botdev"
keyword = "crypto"

# A stupidly wide search across all tweets, posted over the last 30 days
# Maximum 100 tweets
tweets = api.search_30_day(environment_dev, keyword)

percent_verified, number_of_tweets = number_of_verfied_users(tweets)

for tweet in tweets:
    if (tweet.text[0:2] != "RT"):
        n_non_ascii = count_non_ascii(tweet)
        n_hashtags = count_hashtags(tweet)
        if (n_non_ascii <= 2) and (n_hashtags <= 4):
            print_tweet(tweet)

percent_verified, number_of_tweets = number_of_verfied_users(tweets)
print("Out of", number_of_tweets, "tweets,",
        percent_verified, "% were from verified users")

# Test test test
