"""`main` is the top level module for your Bottle application."""

# import the Bottle framework
from bottle import request
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


# serves the data for rendering the main page
@bottle.route('/api/targetAddress')
def getTargetAddress():
	address = PotAddress.getCurrentAddress(startDate)
	data = PotAddress.getData(address)

	# current value of BTC in USD
	BTC_USD = util.getJSON("https://blockchain.info/ticker")['USD']['15m']
	
	output = {
		"secondsLeft":util.getTimeLeft(startDate),
		"address":address,
		"final_balance":data['final_balance'],
		"BTC_USD": BTC_USD,
		"raw": data
	}

	return json.dumps(output)

@bottle.route('/api/ticketsByAddress')
def ticketsByAddress():

	address = request.query.addr
	print 'ticketsByAddress: ' + address

	#TODO: get tickets for a particular address. Keep in mind address can deposit multiple times

	return 'address: ' + address


def determineWinner():
	#TODO: set this function to run as a chron job @ 12 hr interval. Tx might still be pending, so need to re-check
	#TODO: figure out who the winner is
	#TODO: store winner in database or something. maybe send an email to notify me
	#TODO: make sure winning address isn't a mining address. Address must have a transaction input value

	print 'asdf'




	