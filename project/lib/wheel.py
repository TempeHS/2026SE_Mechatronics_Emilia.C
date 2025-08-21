import time
from servo import Servo
from machine import Pin, PWM

class Wheel:
    def __init__(self, pinleft, pinright):
        freq = 50
        min_us = 500
        max_us = 2500
        dead_zone_us = 1500
        self.left_servo = Servo(
            PWM(Pin(pinleft)),
            min_us=min_us,
            max_us=max_us,
            dead_zone_us=dead_zone_us,
            freq=freq
        )
        self.right_servo = Servo(
            PWM(Pin(pinright)),
            min_us=min_us,
            max_us=max_us,
            dead_zone_us=dead_zone_us,
            freq=freq
        )

    def left(self, duration=2.85):
        self.right_servo.set_duty(1300)
        self.left_servo.set_duty(1500)
        time.sleep(duration)

    def right(self, duration=2.25):
        self.right_servo.set_duty(1500)
        self.left_servo.set_duty(1700)
        time.sleep(duration)

    def forward(self, duration=2):
        self.right_servo.set_duty(500)
        self.left_servo.set_duty(2500)
        time.sleep(duration)

    def backward(self, duration=2):
        self.right_servo.set_duty(2500)
        self.left_servo.set_duty(500)
        time.sleep(duration)

    def pause(self, duration=2):
        self.right_servo.set_duty(1500)
        self.left_servo.set_duty(1500)
        time.sleep(duration)

    def stop(self):
        self.right_servo.stop()
        self.left_servo.stop()
        time.sleep(2)