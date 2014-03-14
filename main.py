"""`main` is the top level module for your Bottle application."""

# import the Bottle framework
from bottle import Bottle
import json
import PotAddress
from datetime import datetime
import util

# Create the Bottle WSGI application.
bottle = Bottle()
startDate = datetime(2014, 3, 22)

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.'


# Define an handler for the root URL of our application.
@bottle.route('/api/targetAddress')
def getTargetAddress():
	address = PotAddress.getCurrentAddress(startDate)
	data = PotAddress.getData(address)

	dataDict = json.loads(data);
	dataDict["secondsLeft"] = util.getTimeLeft(startDate)
	print dataDict

	return json.dumps(dataDict)

def determineWinner():
	#TODO: figure out who the winner is
	#TODO: store winner in database or something. maybe send an email to notify me
	print ''
