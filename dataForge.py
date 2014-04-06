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
import numpy
import random
from firebase import firebase

fb = firebase.FirebaseApplication('https://hotspots.firebaseio.com', authentication=None)

sample1T = 'http://distillery.s3.amazonaws.com/media/2011/01/28/0cc4f24f25654b1c8d655835c58b850a_5.jpg'
sample1L = 'http://distillery.s3.amazonaws.com/media/2011/01/28/0cc4f24f25654b1c8d655835c58b850a_6.jpg'
sample1S = 'http://distillery.s3.amazonaws.com/media/2011/01/28/0cc4f24f25654b1c8d655835c58b850a_7.jpg'
sample2T = 'http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_5.jpg'
sample2L = 'http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_6.jpg'
sample2S = 'http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_7.jpg'
sample3T = 'http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_5.jpg'
sample3L = 'http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_6.jpg'
sample3S = 'http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_7.jpg'

randomNames = ['Simon Ayzman','Joseph Wong','Bruce Willis', 'J. J. Abrahms', 'Johnny Depp', 'Swizzle Swazzlepants', 'Steve Jobs']
randomText = [
	'Heyyo there my friend #HackNY',
	'#HackNY all the wayyyyy',
	'I like bubbles',
	'There is no place like #nyc',
	'I love hackNY and nyc',
	'There\'s no place like home',
	'Hacky hack hack NY',
	'Noooo way am I going to javaland',
	'#HackNY is the besttt',
	'Hey derrr bubbles',	
]

result = []
for x in range(0,2):
	randomTweets = []
	for y in range(0,8):
		randomTweets.append({'name' : randomNames[random.randint(0,len(randomNames)-1)], 'text' : randomText[random.randint(0,len(randomText)-1)]})
	resultDict = {'id': x, 
				'lat':39.67 + 2* random.random(),
				'lng':-74.94 + 2* random.random(),
				'tweets':randomTweets,
				'images':[{'low_resolution': {'url' : sample1L, 'width' : 306, 'height' : 306},
							'thumbnail': {'url' : sample1T, 'width' : 150, 'height' : 150},
							'standard_resolution': {'url' : sample1S, 'width' : 612, 'height' : 612}},
							{'low_resolution': {'url' : sample2L, 'width' : 306, 'height' : 306},
							'thumbnail': {'url' : sample2T, 'width' : 150, 'height' : 150},
							'standard_resolution': {'url' : sample2S, 'width' : 612, 'height' : 612}},
							{'low_resolution': {'url' : sample3L, 'width' : 306, 'height' : 306},
							'thumbnail': {'url' : sample3T, 'width' : 150, 'height' : 150},
							'standard_resolution': {'url' : sample3S, 'width' : 612, 'height' : 612}}]
	}
	result.append(resultDict)

fb.put('/','markers',result)

