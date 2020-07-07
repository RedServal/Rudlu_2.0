import tweepy

consumer_key = "XXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

def trump() :
    return api.user_timeline(id='realDonaldTrump', count=1)[0].id