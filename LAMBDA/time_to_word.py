#!/usr/bin/env python
from __future__ import print_function
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import datetime
 
class TimeInWords():
    def __init__(self, time_in_second):
        
        self.words=["one", "two", "three", "four", "five", "six", "seven", "eight","nine", 
       "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
       "twenty two", "twenty three", "twenty four", "twenty five", 
       "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
       	
       	self.dd = datetime.datetime.fromtimestamp(time_in_second)


    def caltime(self):
        
        hrs = self.dd.hour
        mins = self.dd.minute

        if (hrs >12):
            hrs=hrs-12
        if (mins == 0):
            hr = self.words[hrs-1]
            msg = hr + " o'clock."
        elif (mins < 31):      
               hr = self.words[hrs-1]
               mn = self.words[mins-1]
               msg = mn + " past " + hr + "."
        else:
            hr = self.words[hrs]
            mn =self.words[(60 - mins-1)]
            msg = mn + " to " + hr + "."
        return msg

    def calmonth_day(self):

    	month = self.dd.month
    	month = str(month) if(month>9) else "0" + str(month)

    	day = self.dd.day
    	day = str(day) if(day>9) else "0" + str(day)

    	return str(month) + str(day)

'''
if __name__ == '__main__':
    t = TimeInWords(1494436083)
    print (t.caltime())
    print (t.calmonth_day())
'''