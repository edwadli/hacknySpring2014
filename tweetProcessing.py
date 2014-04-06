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

def updateWordHistogram(histogramDictionary,tweetBody):
	keyWordArray = tweetBody.split(" ")
	for word in keyWordArray:
		if len(word) > 4:
			currWord = conditionWord(word)
			if currWord in histogramDictionary.keys():
				histogramDictionary[currWord] += 1
			else:
				histogramDictionary[currWord] = 1

def conditionWord(unconditionedWord):
	word = unconditionedWord
	word = word.lower()
	word = word.translate(None,'`~!@#$%^&*()-_=+[]{};:\",./<>?\|')
	return word

