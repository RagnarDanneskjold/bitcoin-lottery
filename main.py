"""`main` is the top level module for your Bottle application."""

# import the Bottle framework
from bottle import Bottle
import json
import PotAddress
from datetime import datetime
import util
from pprint import pprint

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
	
	output = {
		"secondsLeft":util.getTimeLeft(startDate),
		"address":address,
		"final_balance":dataDict['final_balance']
	}

	return json.dumps(output)

@bottle.route('api/ticketsByAddress')
def ticketsByAddress():
	print 'ticketsByAddress'

	#TODO: get tickets for a particular address. Keep in mind address can deposit multiple times




def determineWinner():
	#TODO: set this function to run as a chron job @ 12 hr interval. Tx might still be pending, so need to re-check
	#TODO: figure out who the winner is
	#TODO: store winner in database or something. maybe send an email to notify me
	print 'asdf'


#TODO: redirect to bitcoin-ticket.custom
# http://stackoverflow.com/questions/1364733/block-requests-from-appspot-com-and-force-custom-domain-in-google-app-engine