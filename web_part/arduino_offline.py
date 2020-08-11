#this is a sample code for testing arduino pin by python....took help from a site..

from pyfirmata2 import Arduino
from time import sleep
board = Arduino(Arduino.AUTODETECT)

switch1=board.digital[9]
switch2=board.digital[10]
switch3=board.digital[11]
switch4=board.digital[13]

switches=switch1,switch2,switch3,switch4

def test_on(*relays):
	[relay.write(1) for relay in relays]
	[print('{} is turned on'.format(relay)) for relay in relays]

def on(relays):
	[relay.write(1) for relay in relays]
	[print('{} is turned on'.format(relay)) for relay in relays]


def off():
	[switch.write(0) for switch in switches]		

test_on(switch1,switch2,switch3,switch4)
sleep(10)
off()
sleep(10)	