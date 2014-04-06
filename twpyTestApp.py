import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
twitter_consumer_key = 'T0foLprojTuyETudVyaUPYUeP'
twitter_consumer_secret = 'nmY0z8LClJr1vuTUCnIORsiFtaTzW6ckVJDvj60ATMXryhlQlw'

twitter_access_token = '719330150-eM3GGu06smiyVBu6qp09acCP1YTmULr50ftvytAq'
twitter_access_token_secret = 'atlE2CeabrB49A9ld0meSZinWPBSl9aslW5KoTwBHBX3H'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    auth.set_access_token(twitter_access_token, twitter_access_token_secret)

    print "Showing all new tweets for #programming:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    #stream = tweepy.Stream(auth, l)
    #stream.filter(track=['hackNY'])
        #,locations=[-74,40,-73,41])
    api = tweepy.API(auth)
    for tweet in api.search(q='', count=200, geolocation='40.6700,73.9400,100mi'):
        try:
            if tweet.coordinates != None:
                print tweet.coordinates,tweet.text
        except:
            print
    #nothing
    