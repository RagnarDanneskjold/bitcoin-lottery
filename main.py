"""`main` is the top level module for your Bottle application."""

# import the Bottle framework
from bottle import Bottle
import urllib2
import json

# Create the Bottle WSGI application.
bottle = Bottle()

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.'


# Define an handler for the root URL of our application.
@bottle.route('/api/targetAddress')
def getTargetAddress():
	address = '1Gt3aEWRp3kPwimW8KTxjGQZ8u7TtsaLU6'
	data = getAddressData(address)
	return data

def getAddressData(address):

	url = 'http://blockchain.info/address/' + address + '?format=json'

	req = urllib2.Request(url)
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
	
	return response

def determineWinner():
	#TODO: figure out who the winner is
	print ''