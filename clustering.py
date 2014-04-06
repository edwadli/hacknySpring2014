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


