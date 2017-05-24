#!/usr/bin/env python
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime 
from database import initialize_db
import json


def Fetch( count = 2, status = 'recent', type = 'all', now = 1494436083, DEPLOY = False):

	db = initialize_db.DynamoDB('competitons_', DEPLOY = DEPLOY)

	#getting the current time
	now = datetime.now()
	epoch = datetime.utcfromtimestamp(0)
	now = now - epoch
	now = int(now.total_seconds())


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
		del KKe

	_x = len(response) if len(response)<= count else count
	response = response[0:_x]
	del db, now, epoch, Fe, Ke, _x
	#print (response)

	return response

#Fetch(status = 'future' ,DEPLOY = True)