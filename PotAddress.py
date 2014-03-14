from datetime import datetime
import urllib2
import util

#TODO: rename this class to something else... DeopsitAddress

addressList = [
	'1Gt3aEWRp3kPwimW8KTxjGQZ8u7TtsaLU6', #test
	'1MoFF5TTuy6rcFyLGbfqycSowcrzJvdE19', #1
	'1BNF3rDhQLhtDJg9f18Q71m6D6ezPXDGAy',
	'12V9kthXPoXkgGPfP7cfNXGv3yTXZ1SFWL',
	'15tBLmdab8PLr9nj2yLTUGy8JjaNmbaQaH',
	'1EAMkussm4smads4yAoCGHAQ6DBrmSG7N6',
	'1993qZ3pT4aknou1631yNGerB33iEHxy92',
	'1KQpsoAhRwgyUGTxUuYfAzRxL3kYLTLqVf',
	'124UQePHLadZU5qbmShvzd4TvPE92NicXV',
	'17tT2sQU1pvDuDM65gfQwZu7dWVNN25LUoTC',
	'14ns361B7wsL3WFtMFvwmxfthGqAAE3mXt', #10
]

# gets the current deposit address depending on the week.
def getCurrentAddress(startDate):
	currentWeek = util.getCurrentWeek(startDate)
	print 'currentWeek: ' + str(currentWeek)
	return addressList[currentWeek];

def getData(address):

	url = 'http://blockchain.info/address/' + address + '?format=json'

	req = urllib2.Request(url)
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
	
	return response