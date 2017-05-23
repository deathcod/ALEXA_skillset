#!/usr/bin/env python
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime 
from database import initialize_db
import json

DEPLOY = True
db = initialize_db.DynamoDB('competitons_', DEPLOY = DEPLOY)

def Fetch( count = 'two', status = 'recent', type = 'all'):

	#getting the cuurent time
	now = datetime.now()
	epoch = datetime.utcfromtimestamp(0)
	now = now - epoch
	now = int(now.total_seconds())


	#testing!!
	#now = 1494436083

	#Setting default value for FilterExpresion
	Fe = None

	# True : Ascending, False : Descending
	#Setting default value for ScanIndexForward
	sort = True
	if status == 'future':
		Ke = Key('start_time').gt(now)
		sort = False
	elif status == 'ongoing':
		Ke = Key('start_time').lte(now)
		Fe = Attr('end_time').gt(now)
	else:
		Ke = Key('start_time').gt(now)


	#Setting default value for no_of_count
	no_of_count = 2

	if count == 'one' : 
		no_of_count = 1
	elif count == 'two' :
		no_of_count = 2
	elif count == 'three' :
		no_of_count = 3
	elif count == 'four':
		no_of_count = 4
	elif count == 'five':
		no_of_count = 5
	elif count == 'six':
		no_of_count = 6
	elif count == 'seven':
		no_of_count = 7
	elif count == 'eight':
		no_of_count = 8
	elif count == 'nine':
		no_of_count = 9
	else:
		no_of_count = 10


	if type == 'hackathon':
		Ke &= Key('classification').eq('h')
		response = json.loads(db.query_data(Ke, Fe, sort))

	elif type == 'coding' or type == 'algorithmic' or type == 'competitive programming':
		Ke &= Key('classification').eq('cp')
		response = json.loads(db.query_data(Ke, Fe, sort))

	else:
		KKe = Ke & Key('classification').eq('cp')
		response = json.loads(db.query_data(KKe, Fe, sort))

		KKe = Ke & Key('classification').eq('h')
		response += json.loads(db.query_data(KKe, Fe, sort))

		#write lambda function to sort the values according to the sort given
		response = sorted(response, key = lambda x : x['start_time'], reverse = not sort) #reverse = True : descending, so using opposite of sort

	x = len(response) if len(response)<= no_of_count else no_of_count
	response = response[0:x]
	#print (response)

	return response

# Fetch(status = 'future' )