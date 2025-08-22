import time
from wheel import Wheel
from machine import Pin, PWM


pinR = PWM(Pin(18))
pinL = PWM(Pin(20))

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

pinRight = Wheel(
    pwm=pinR, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

pinLeft = Wheel(
    pwm=pinL, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

def forward():
    pinR.set_duty(500)
    pinL.set_duty(2500)
    time.sleep(2)

def left():
    pinR.set_duty(1300)
    pinL.set_duty(1500)
    time.sleep(2.85)

def right():
    pinR.set_duty(1500)
    pinL.set_duty(1700)
    time.sleep(2.25)

def backward():
    pinR.set_duty(2500)
    pinL.set_duty(500)
    time.sleep(2)

def pause():
    pinR.set_duty(1500)
    pinL.set_duty(1500)
    time.sleep(2)

def stop():
    pinR.stop()
    pinL.stop()
    time.sleep(2)


forward()
left()
right()
right()
backward()
stop()