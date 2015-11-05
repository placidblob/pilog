import threading
from time import sleep
from random import randint, random
import pifacedigitalio
import sys

NUM_MOLES = 4  # max 4


class Mole(object):
    def __init__(self, number, pifacedigital):
        led_start_index = number
        self.led = pifacedigital.leds[led_start_index] #,
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

    def hit(self):
        """Attempt to hit a mole, return success."""
        if self.hiding:
            return False
        else:
            self.hide()
            return True


class WhackAMoleGame(object):
    def __init__(self):
        self.should_stop = False
        self.pifacedigital = pifacedigitalio.PiFaceDigital()
        self.moles = [Mole(i, self.pifacedigital) for i in range(NUM_MOLES)]
        self._current_points = 0
        self.max_points = 0
        self.inputlistener = \
            pifacedigitalio.InputEventListener(chip=self.pifacedigital)
        for i in range(4):
            self.inputlistener.register(
                i, pifacedigitalio.IODIR_FALLING_EDGE, self.hit_mole)
        self.inputlistener.activate()

    def start(self):
        while not self.should_stop:
            # randomly moves moles up and down
            for mole in self.moles:
                should_hide = (randint(0, 1) == 1)
                mole.hiding = should_hide

            #sleep(random() * 3)
            sleep(1)
        self.inputlistener.deactivate()
        self.flash_leds()

    @property
    def points(self):
        return self._current_points

    @points.setter
    def points(self, new_value):
        if self.max_points > 1 and new_value <= 1:
            self.should_stop = True  # end the game
            return

        self.max_points = max(self.max_points, new_value)
        self._current_points = new_value

    def hit_mole(self, event):
        # print("You pressed", event.pin_num)
        if game.moles[event.pin_num].hit():
            goame.points += 1
            print("You hit a mole!")
        else:
            game.points -= 1
            print("You missed!")

    def flash_leds(self):
        self.pifacedigital.output_port.all_on()
        for i in range(10):
            self.pifacedigital.output_port.toggle()
            sleep(0.1)
        self.pifacedigital.output_port.all_off()

    def all_off(self):
        self.pifacedigital.output_port.all_off()


if __name__ == "__main__":
    game = WhackAMoleGame()
    try:
        game.start()
        print("You scored {}!".format(game.max_points))
    except :
        print("bye")
        game.all_off()
        sys.exit(0)
        sys.exit(0)