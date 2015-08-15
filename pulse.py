'''
Copyright 2015 (c) Eli Levin

pulse.py - makes a color "pulse" by looping brightness and saturation
'''

from phue import Bridge
import time
import math

b = Bridge('192.168.1.9') # Enter bridge IP here.


b.create_group('myLights', [1,2,3])

lights = b.lights # get a list of all lights

def set_hue(hueVal):
	#set hue for a group of lights
	b.set_group(1,'hue',hueVal)

def set_bri(briVal):
	#set brightness for a group of lights
	b.set_group(1,'bri',briVal)

def set_sat(satVal):
	#set saturation for a group of lights
	b.set_group(1,'sat',satVal)

def set_timing(transVal):
	#set transition time for a group of lights
	b.set_group(1,'transitiontime',transVal)

keepSwitching = True
myHue = 0
TRANSITION_TIME = 100 #100
set_timing(TRANSITION_TIME)
set_hue(myHue)

#start pulse loop
while keepSwitching:
	if lights[0].hue == myHue:
		# l.brightness = 164 #TODO: replace with adjusting built-in transition time
		myHue += 2400

		if myHue > 65280:
			myHue = 0

		
		set_hue(myHue)
		#time.sleep(2)