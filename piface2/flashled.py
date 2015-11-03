# remember to do: apt-get install python3-pifacedigitalio

import pifacedigitalio
from time import sleep

pfd = pifacedigitalio.PiFaceDigital()
try:
	while(True):
		pfd.output_pins[0].value = not pfd.output_pins[0].value
		sleep(0.5)
finally:
	# be polite and leave the LED off when exiting
	pfd.output_pins[0].value = 0