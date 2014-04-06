import tweepy
import json
import globeDist
import time
import re
import urllib2
from firebase import firebase

heatmap_coords = {}
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

pNum = re.compile('-?\d+.\d+')
pLat = re.compile('USER_LAT:\s-?\d+.\d+,')
pLng = re.compile('USER_LNG:\s-?\d+.\d+,')

def updateFirebase(myLat, myLng, myRad):
    
    loc = str(myLat) + ',' + str(myLng) + ',' + str(myRad/2.0) + 'mi'
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
    count = 0
    myTwts = api.search(q='4sq.com', geocode=loc, count=100)
    for i, tweet in enumerate(myTwts):
        count += 1
        #print 'Tweet', tweet.text.encode('ascii', 'ignore')
        url = re.findall('t.co/\w+',
                        tweet.text)
        if tweet.coordinates != None:
            coords = tweet.coordinates['coordinates']
            post_result = fb.put('/heatmap/', tweet.id, {'lng':coords[0],
                                    'lat':coords[1]})
            # print post_result
            # heatmap_coords[tweet.id] = {'lng':coords[0],
            #                         'lat':coords[1]}
            # heatmap_coords.append({'lng':coords[0],
            #                         'lat':coords[1],
            #                         'id': i})
        elif url:
            try:
                the_html = urllib2.urlopen("http://" + url[0]).read()
                #print the_html
                lat = float(pNum.search(pLat.search(the_html).group()).group())
                lng = float(pNum.search(pLng.search(the_html).group()).group())
                coords = tweet.coordinates['coordinates']
                post_result = fb.put('/heatmap/', tweet.id, {'lng':coords[0],
                                        'lat':coords[1]})
                # heatmap_coords[tweet.id] = {'lng':lng,
                #                         'lat':lat}
                # heatmap_coords.append({'lng':lng,
                #                         'lat':lat,
                #                         'id': i})
            except:
                print "404 caught", tweet.text.encode('ascii', 'ignore')
            #print '%s %s %s' %(tweet.created_at, tweet.text.encode('ascii', 'ignore'), tweet.coordinates['coordinates'])
    #print "The count is" + str(count)
    return heatmap_coords


def callback_renewBounds(events):
    print "event", events
    fb_bounds = events
    NE = fb_bounds[0]
    SW = fb_bounds[1]
    print NE
    print SW

    myRad = globeDist.dis(NE['lat'],NE['lng'],SW['lat'],SW['lng'])/2.0

    print myRad

    myLat = (NE['lat']+SW['lat'])/2.0
    myLng = (NE['lng']+SW['lng'])/2.0

    heatmap_coords = updateFirebase(myLat, myLng, myRad)
    # post_result = fb.put('/heatmap/', tweet.id, heatmap_coords)
    # print post_result


if __name__ == '__main__':
    #fb.get_async('/bounds',None,callback=callback_renewBounds)
    fb.put('/', 'changed', True)
    while True:
        if fb.get('/changed', None):
            fb.put('/', 'changed', False)
            fb.get_async('/bounds',None,callback=callback_renewBounds)


