'''
color_pulse makes a group of bulbs pulsate in synchronous colors at different
color saturations and pulse speed
'''

from phue import Bridge
import random

b = Bridge('192.168.1.9') # Enter bridge IP here.

lights = b.lights # get a list of all lights

#set all transition times to 100
# for l in lights:
# 	l.transitiontime = 100

keepSwitching = True
#start pulse loop
while keepSwitching:
	color_xy = [random.random(), random.random()]

	for l in lights:
		l.brightness = 120
		l.xy = color_xy

	quitString = raw_input('q to quit; enter to change colors: ')
	if quitString == "q":
		keepSwitching = False