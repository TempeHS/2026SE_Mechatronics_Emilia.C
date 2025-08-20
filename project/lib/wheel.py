import time
from servo import Servo
from machine import Pin, PWM

class Wheel:
    def __init__(self, pinleft, pinright, debug=False):
        self.__debug = debug
        self.pinL = PWM(Pin(20))
        self.pinR = PWM(Pin(18))
        self.pinL.freq(50)
        self.pinR.freq(50)

    def left(self):
        if self.__debug:
            self.pinR.set_duty(1300)
            self.pinL.set_duty(1500)
            time.sleep(2.85)

    def right(self):
        if self.__debug:
            self.pinR.set_duty(1500)
            self.pinL.set_duty(1700)
            time.sleep(2.25)

    def forward(self):
        if self.__debug:
            self.pinR.set_duty(500)
            self.pinL.set_duty(2500)
            time.sleep(2)

    def backward(self):
        if self.__debug:
            self.pinR.set_duty(2500)
            self.pinL.set_duty(500)
            time.sleep(2)

    def pause(self):
        if self.__debug:
            self.pinR.set_duty(1500)
            self.pinL.set_duty(1500)
            time.sleep(2)

    def stop(self):
        if self.__debug:
            self.pinR.stop()
            self.pinL.stop()
            time.sleep(2)