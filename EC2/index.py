#!/usr/bin/env python
import os, sys
import logging
from concurrent import futures

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from database import initialize_db
from src import scrapping_sites


logging.basicConfig(level=logging.INFO)

#True is used when it has to be deployed otherwise it is False for local testing

def multithreading(DEPLOY):
	global database

	logging.info("Concurrently scrape and transfer to DynamoDb")
	with futures.ThreadPoolExecutor(max_workers = 6) as pool:
		running = [ pool.submit(scrapping_sites.codeforces, DEPLOY),
					pool.submit(scrapping_sites.codechef, DEPLOY),
					pool.submit(scrapping_sites.venturesity, DEPLOY),
					pool.submit(scrapping_sites.analyticsvidhya, DEPLOY),
					pool.submit(scrapping_sites.devpost, DEPLOY),
					pool.submit(scrapping_sites.techgig, DEPLOY)]

		for future in futures.as_completed(running):
			data = future.result()
			database.put_data(data)
			pass
		pass
	pass



"""
Multithreading
real	0m48.104s
user	0m2.136s
sys		0m0.112s
"""
DEPLOY = True
database = initialize_db.DynamoDB('competitons_', DEPLOY = DEPLOY)
multithreading(DEPLOY = DEPLOY)

"""
Sequential
real	2m4.932s
user	0m2.096s
sys		0m0.108s
"""
# DEPLOY = True
# x = initialize_db.DynamoDB('competitons_', DEPLOY = DEPLOY)
# x.put_data(scrapping_sites.codeforces(DEPLOY = DEPLOY))
# x.put_data(scrapping_sites.codechef(DEPLOY = DEPLOY))
# x.put_data(scrapping_sites.venturesity(DEPLOY = DEPLOY))
# x.put_data(scrapping_sites.analyticsvidhya(DEPLOY = DEPLOY))
# x.put_data(scrapping_sites.devpost(DEPLOY = DEPLOY))
# x.put_data(scrapping_sites.techgig(DEPLOY = DEPLOY))