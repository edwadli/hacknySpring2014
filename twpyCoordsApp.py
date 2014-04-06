import tweepy
import json
import globeDist
from firebase import firebase

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'T0foLprojTuyETudVyaUPYUeP'
consumer_secret = 'nmY0z8LClJr1vuTUCnIORsiFtaTzW6ckVJDvj60ATMXryhlQlw'

access_token = '719330150-eM3GGu06smiyVBu6qp09acCP1YTmULr50ftvytAq'
access_token_secret = 'atlE2CeabrB49A9ld0meSZinWPBSl9aslW5KoTwBHBX3H'

#firebase connection
fb = firebase.FirebaseApplication('https://hotspots.firebaseio.com',
                authentication=None)

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

def updateFirebase(myLat, myLng, myRad):
    
    loc = str(myLng) + ',' + str(myLat) + ',' + str(myRad) + 'mi'
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets in radius:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    #stream = tweepy.Stream(auth, l)
    #stream.filter(track=['hackNY'])
        #,locations=[-74,40,-73,41])
    api = tweepy.API(auth)

    heatmap_coords = []
    myTwts = api.search(geocode=loc, count=50)
    for i, tweet in enumerate(myTwts):
        #print tweet.entities
        #break
        if tweet.coordinates != None:
            coords = tweet.coordinates['coordinates']
            heatmap_coords.append({'lng':coords[0],
                                    'lat':coords[1],
                                    'id': i})
            #print '%s %s %s' %(tweet.created_at, tweet.text.encode('ascii', 'ignore'), tweet.coordinates['coordinates'])
    return heatmap_coords


def callback_renewBounds(response):
    fb_bounds = fb.get('/bounds', None)
    NE = fb_bounds[0]
    SW = fb_bounds[1]
    print NE
    print SW

    myRad = globeDist.dis(NE['lat'],NE['lng'],SW['lat'],SW['lng'])/2.0

    print myRad

    myLat = (NE['lat']+SW['lat'])/2.0
    myLng = (NE['lng']+SW['lng'])/2.0

    heatmap_coords = updateFirebase(myLat, myLng, myRad)
    post_result = fb.put('/', 'heatmap', heatmap_coords)
    print post_result

if __name__ == '__main__':
    while True:
        fb.get_async('/bounds',None,callback=callback_renewBounds)
    
