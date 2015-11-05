import threading
from time import sleep
from random import randint, random
import pifacedigitalio
import sys

NUM_MOLES = 8  # max 4


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

    def off(self):
        self.led.turn_off()
        self._is_active = False

    def on(self):
        self.led.turn_on()
        self._is_active = True

    def toggle(self):
        self.active = not self.active


class Maestro(object):
    def __init__(self):
        # init piface
        self.pifacedigital = pifacedigitalio.PiFaceDigital()

        # framework init
        self.leds = [LED(i, self.pifacedigital) for i in range(NUM_MOLES)]

        # output init
        self.inputlistener = pifacedigitalio.InputEventListener(chip=self.pifacedigital)
        for i in range(4):
            self.inputlistener.register(
                i, pifacedigitalio.IODIR_FALLING_EDGE, self.hit_mole)
        self.inputlistener.activate()

    def hit_mole(self, event):
        print("You pressed", event.pin_num)

    def flash_leds(self):
        self.pifacedigital.output_port.all_on()
        for i in range(10):
            self.pifacedigital.output_port.toggle()
            sleep(0.1)
        self.pifacedigital.output_port.all_off()

    def all_off(self):
        self.pifacedigital.output_port.all_off()

    def do_your_thing(self):
        for i in range(NUM_MOLES):
            self.leds[i].toggle()
            sleep(1)
        self.flash_leds()


if __name__ == "__main__":
    game = Maestro()
    try:
        game.do_your_thing()
    except :
        print("bye")
        game.all_off()
        sys.exit(0)
        sys.exit(0)