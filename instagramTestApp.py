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

DIST = str(5000)
TIME_LAPSE = 6 # in hours

#nycLat = str(40.805406700000000000)
#nycLng = str(-73.961330699999960000)

def getData(lat,lng):
	time = str(calendar.timegm((datetime.datetime.now() - datetime.timedelta(hours=TIME_LAPSE)).utctimetuple()))
	getInfo = urllib2.urlopen('https://api.instagram.com/v1/media/search?lat=' + lat + '&lng=' + lng + '&distance=' + DIST + '&min_timestamp='+ time + '&client_id=' + instagram_client_key).read()
	return json.loads(getInfo)['data']


def getInstagramURLSForCoordinateAndHashtag(lat,lng,tag):
	images = []
	data = getData(lat,lng)
	for post in data:
		if tag in post['tags']:
			images.append(post['images']);
	return images

#print getInstagramURLSForCoordinateAndHashtag(nycLat,nycLng,'nyc')
