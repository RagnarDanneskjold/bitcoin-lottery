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

	# userAddr = request.query.addr
	userAddr = '1669MUGQDuC1hzyvHg7bqWDUZCCNYoQqvf'

	print 'ticketsByAddress: ' + userAddr

	#TODO: get tickets for a particular address. Keep in mind address can deposit multiple times
	potAddr = PotAddress.getCurrentAddress(startDate)
	potAddrData = PotAddress.getData(potAddr)

	#expect 1 from Thcdk
	#expect 3 from YoQqvf

	btcDeposited = 0

	for tx in potAddrData['txs']:
		print ""
		print 'checking transaction for...'
		print tx['inputs'][0]['prev_out']['addr']
		if(tx['inputs'][0]['prev_out']['addr'] == userAddr):
			print tx['out'][0]['value']
			btcDeposited += tx['out'][0]['value']

	return str(btcDeposited)


def determineWinner():
	#TODO: set this function to run as a chron job @ 12 hr interval. Tx might still be pending, so need to re-check
	#TODO: figure out who the winner is
	#TODO: store winner in database or something. maybe send an email to notify me
	#TODO: make sure winning address isn't a mining address. Address must have a transaction input value

	print 'asdf'




