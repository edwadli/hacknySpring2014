#! /usr/bin/python

import types
import sys
import json
import simplejson
import time
import getpass
import unittest
import urlparse
import datetime
import calendar
import urllib2
from instagram.client import InstagramAPI
from instagram import client, oauth2, InstagramAPIError

instagram_client_key = 'f4c597a88f114c0ba8eb949d54336a58'
instagram_client_secret = 'c4b0f208cda64720b534fc14b126007b'

lat = str(40.805406700000000000)
lng = str(-73.961330699999960000)
dist = str(5000)
time = str(calendar.timegm((datetime.datetime.now() - datetime.timedelta(hours=24)).utctimetuple()))

getInfo = urllib2.urlopen('https://api.instagram.com/v1/media/search?lat=' + lat + '&lng=' + lng + '&distance=' + dist + '&min_timestamp='+ time + '&client_id=' + instagram_client_key).read()
data = json.loads(getInfo)['data']
for post in data:
	print '[', str(post['location']['latitude']),',', str(post['location']['longitude']), ']', post['user']['username'], post['tags']

#print content
#api = InstagramAPI(client_id=instagram_client_key, client_secret=instagram_client_secret)
#print time
#recents = api.media_search(lat=37.7,lng=-122.22,min_timestamp=time,distance=5000)
#print recents
#locations = api.location_search(lat=40.6700,lng=73.9400, distance=5000)
#media = []
#for media_item in recents:
#	media.append(api.media_search(lat=37.7,lng=-122.22,min_timestamp=calendar.timegm(time),distance=5000))

#api.create_subscription(object='location', object_id='1257285', aspect='media', callback_url='http://mydomain.com/hook/instagram')
# Subscribe to all media in a geographic area
#api.create_subscription(object='geography', lat=35.657872, lng=139.70232, radius=1000, aspect='media', callback_url='http://mydomain.com/hook/instagram')