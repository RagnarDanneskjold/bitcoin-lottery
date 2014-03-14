from datetime import datetime
from datetime import timedelta
import math

def getCurrentWeek(startDate):
	daysElapsed = (datetime.now() - startDate).days;
	return max(daysElapsed/7, 0)

def getTimeLeft(startDate):
	currWeek = getCurrentWeek(startDate)
	nextWeekDate = startDate + timedelta(weeks=currWeek+1);
	timeLeft = nextWeekDate - datetime.now()
	
	return math.floor(timeLeft.total_seconds())
