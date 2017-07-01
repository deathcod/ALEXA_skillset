#!/usr/bin/env python
import logging
import os
import sys
from concurrent import futures

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from database import initialize_db
from src import scrapping_sites

logging.basicConfig(level=logging.INFO)

# True is used when it has to be deployed otherwise it is False for local testing

DEPLOY = True
database = initialize_db.DynamoDB('competitons_', DEPLOY=DEPLOY)


def multithreading(DEPLOY=False):
    global database
    combine_data = {}
    logging.info("Concurrently scrape and transfer to DynamoDb")
    with futures.ThreadPoolExecutor(max_workers=6) as pool:
        running = [pool.submit(scrapping_sites.codeforces, DEPLOY),
                   pool.submit(scrapping_sites.codechef, DEPLOY),
                   pool.submit(scrapping_sites.venturesity, DEPLOY),
                   pool.submit(scrapping_sites.analyticsvidhya, DEPLOY),
                   pool.submit(scrapping_sites.devpost, DEPLOY),
                   pool.submit(scrapping_sites.techgig, DEPLOY)]

        for future in futures.as_completed(running):
            # using put item
            # pool.submit(database.put_data, future.result())

            # using batch write item
            pool.submit(database.batch_write, future.result())
            pass
        pass
    pass


def sequential(DEPLOY=False):
    global database

    logging.info("Sequential scrape and transfer to DynamoDb")
    database.put_data(scrapping_sites.codeforces(DEPLOY=DEPLOY))
    database.put_data(scrapping_sites.codechef(DEPLOY=DEPLOY))
    database.put_data(scrapping_sites.venturesity(DEPLOY=DEPLOY))
    database.put_data(scrapping_sites.analyticsvidhya(DEPLOY=DEPLOY))
    database.put_data(scrapping_sites.devpost(DEPLOY=DEPLOY))
    database.put_data(scrapping_sites.techgig(DEPLOY=DEPLOY))
    pass


"""
Multithreading using put item
real	0m48.104s
user	0m2.136s
sys		0m0.112s

Multithreading using batch write item
real    0m4.572s
user    0m1.168s
sys     0m0.080s

"""
multithreading(DEPLOY=DEPLOY)

"""
Sequential using put item
real	2m4.932s
user	0m2.096s
sys		0m0.108s
"""
# sequential(DEPLOY=DEPLOY)
