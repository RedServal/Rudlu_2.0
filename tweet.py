import tweepy

consumer_key = "AGL0YXlKhfnT9P7MjgEA8sVkX"
consumer_secret = "DBT5bLQrYpArEsVFJtUW2lwCFvvnBb1vjbEBztC2cVz2lyqv6l"
access_token = "1544061794-N9WzcYP8AVWqyQkapru6EIsH82XYiLPPaHAL5uC"
access_token_secret = "lqltp0GxxKln5cUlClW0hH7MtreuzrCRmnPC8Zxlor3us"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
"""
tweets = []
username = 'realDonaldTrump'
count = 1
try: 
# Pulling individual tweets from query
    for tweet in api.user_timeline(id=username, count=count):# Adding to list that contains all tweets
        tweets.append((tweet.created_at,tweet.id,tweet.text))
    print(tweets)
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)
"""
"""
def trump() :
    tweets = []
    username = 'realDonaldTrump'
    for tweet in api.user_timeline(id=username, count=1):# Adding to list that contains all tweets
        tweets.append((tweet.created_at,tweet.id,tweet.text))
    print(tweets[0][1])
"""

def trump() :
    return api.user_timeline(id='realDonaldTrump', count=1)[0].id