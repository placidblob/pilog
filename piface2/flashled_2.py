# source: http://www.piface.org.uk/assets/docs/PiFace-Digital2_getting-started.pdf
# remember to do: apt-get install python3-pifacedigitalio

import pifacedigitalio
from time import sleep

pfd = pifacedigitalio.PiFaceDigital()
i = 0
try:
    while(True):
        pfd.output_pins[0].value = not pfd.output_pins[0].value
        i += 1
        slp = abs(50 - (i % 100))
        sleep(slp / 100.0)
finally:
    # be polite and leave the LED off when exiting
    pfd.output_pins[0].value = 0