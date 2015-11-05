import threading
from time import sleep
from random import randint, random
import pifacedigitalio
import sys

NUM_MOLES = 8  # max 4


class Mole(object):
    def __init__(self, number, pifacedigital):
        self.led = pifacedigital.leds[number]
        self.hiding = True

    @property
    def hiding(self):
        return self._is_hiding

    @hiding.setter
    def hiding(self, should_hide):
        if should_hide:
            self.hide()
        else:
            self.show()

    def hide(self):
        self.led.turn_off()
        self._is_hiding = True

    def show(self):
        self.led.turn_on()
        self._is_hiding = False

    def toggle(self):
        self.hiding = not self.hiding


class WhackAMoleGame(object):
    def __init__(self):
        #local variables
        self.should_stop = False

        # init piface
        self.pifacedigital = pifacedigitalio.PiFaceDigital()

        # framework init
        self.moles = [Mole(i, self.pifacedigital) for i in range(NUM_MOLES)]

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
            self.moles[i].toggle()
            sleep(1)
        self.flash_leds()


if __name__ == "__main__":
    game = WhackAMoleGame()
    try:
        game.do_your_thing()
    except :
        print("bye")
        game.all_off()
        sys.exit(0)
        sys.exit(0)