#!/usr/bin/env python
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime 
from database import initialize_db

DEPLOY = True
db = initialize_db.DynamoDB('competitons_', DEPLOY = DEPLOY)

def fetch( count = 'two', status = 'recent', type = 'all'):

	#getting the cuurent time
	now = datetime.now()
	epoch = datetime.utcfromtimestamp(0)
	now = now - epoch
	now = int(now.total_seconds())


	#testing!!
	#now = 1494436083


	# True : Ascending, False : Descending
	sort = True
	if status == 'future':
		fe = Key('start_time').gt(now)
		sort = False
	elif status == 'ongoing':
		fe = Key('start_time').lte(now) & Key('end_time').gt(now)
	else:
		fe = Key('start_time').gt(now)


	if type == 'hackathon':
		fe &= Attr('classification').eq('h')
	elif type == 'coding' or type == 'algorithmic' or type == 'competitive programming':
		fe &= Attr('classification').eq('cp')
	

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

	response = db.scan_data(fe, sort, count)


fetch()