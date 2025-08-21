import time
from servo import Servo
from machine import Pin, PWM

class Wheel:
    def __init__(self, pinleft, pinright):
        self.left_servo = Servo(PWM(Pin(pinleft)))
        self.right_servo = Servo(PWM(Pin(pinright)))

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