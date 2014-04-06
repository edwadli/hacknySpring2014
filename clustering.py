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
from instagram.client import InstagramAPI
from instagram import client, oauth2, InstagramAPIError

#takes an array of dictionaries with 'lat' and 'lng' keys
def calculateMarkerPointFromRelatedCoordinated(coordinateArray):
	finalPoint = { 'lat' : 0, 'lng' : 0}
	latitudes = []
	longitudes = []
	for point in coordinateArray:
		latitudes.append(point['lat'])
		longitudes.append(point['lng'])
	latMean = numpy.mean(latitudes)
	latStd = numpy.std(latitudes)
	lngMean = numpy.mean(longitudes)
	lngStd = numpy.std(longitudes)
	sumLats = 0.0
	sumLngs = 0.0
	count = 0
	for coordinate in coordinateArray:
		currLat = coordinate['lat']
		currLng = coordinate['lng']
		if latMean + 1.5 * latStd > currLat and latMean - 1.5 * latStd < currLat and lngMean + 1.5 * lngStd > currLng and lngMean - 1.5 * lngStd < currLng:
			sumLats += currLat
			sumLngs += currLng
			count += 1
	print count
	return { 'lat' : sumLats / count, 'lng' : sumLngs / count}

'''
points = [
			{
				'lat' : 40.57886,
				'lng' : -73.345
			},
			{
				'lat' : 40.57886,
				'lng' : -73.345
			},
			{
				'lat' : 41.243,
				'lng' : -73.345
			},
			{
				'lat' : 20.93242,
				'lng' : 49.45345
			},
			{
				'lat' : 40.57886,
				'lng' : -73.345
			},
			{
				'lat' : 40.57886,
				'lng' : -74.54
			}
		]
print calculateMarkerPointFromRelatedCoordinated(points)'''
