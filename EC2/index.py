#!/usr/bin/env python
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from database import initialize_db
from src import scrapping_sites

DEPLOY = True
x = initialize_db.DynamoDB('competitons_', DEPLOY = DEPLOY)
x.put_data(scrapping_sites.codeforces(DEPLOY = DEPLOY))
x.put_data(scrapping_sites.codechef(DEPLOY = DEPLOY))
x.put_data(scrapping_sites.venturesity(DEPLOY = DEPLOY))