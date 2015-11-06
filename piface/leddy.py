import threading
from time import sleep
from random import randint, random
import pifacedigitalio
import sys

NUM_LEDS = 8  # max 4
NUM_LOOPS = 100
BLINK=0.015

class LED(object):
    def __init__(self, number, pifacedigital):
        self.led = pifacedigital.leds[number]
        self._is_active = False

    @property
    def active(self):
        return self._is_active

    @active.setter
    def active(self, should_show):
        if should_show:
            self.on()
        else:
            self.off()

    def off(self, send=True):
        if send:
            self.led.turn_off()
        self._is_active = False

    def on(self, send=True):
        if send:
            self.led.turn_on()
        self._is_active = True

    def toggle(self):
        self.active = not self.active


class Maestro(object):
    def __init__(self):
        # init piface
        self.pifacedigital = pifacedigitalio.PiFaceDigital()

        # framework init
        self.leds = [LED(i, self.pifacedigital) for i in range(NUM_LEDS)]

        # output init
        self.inputlistener = pifacedigitalio.InputEventListener(chip=self.pifacedigital)
        for i in range(4):
            self.inputlistener.register(
                i, pifacedigitalio.IODIR_FALLING_EDGE, self.btn_press)
        self.inputlistener.activate()

    def btn_press(self, event):
        print(event.pin_num + 1)
        self.do_your_thing(event.pin_num + 1)

    def all_off(self):
        self.pifacedigital.output_port.all_off()
        for l in self.leds:
            l.off(False)

    def do_your_thing(self, num_times = 1):
        for k in range(num_times):
            for i in range(NUM_LEDS * 2):
                self.leds[i % NUM_LEDS].toggle()
                sleep(BLINK)
            sleep(BLINK)
        self.all_off()


if __name__ == "__main__":
    game = Maestro()
    try:
        game.do_your_thing()
    except :
        print("bye")
        game.all_off()
        sys.exit(0)