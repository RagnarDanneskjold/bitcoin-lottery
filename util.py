from datetime import datetime
from datetime import timedelta
import math
import urllib2
import json

def getCurrentWeek(startDate):
	daysElapsed = (datetime.now() - startDate).days;
	return max(daysElapsed/7, 0)

# returns time remaining in the week
def getTimeLeft(startDate):
	currWeek = getCurrentWeek(startDate)
	nextWeekDate = startDate + timedelta(weeks=currWeek+1);
	timeLeft = nextWeekDate - datetime.now()
	
	return math.floor(timeLeft.total_seconds())

def getJSON(url):
	req = urllib2.Request(url)
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
	return json.loads(response)