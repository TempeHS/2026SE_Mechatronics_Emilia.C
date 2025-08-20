"""
Sample code for servo library, demonstrating instantiation
and setting angles for a continuous servo the resulting wheel speed
of a set_duty(x) call are:

| Set duty |  Speed  | Direction |
| -------- | ------- | --------- |
|   500    | Fast    | Backward  |
|   1400   | Slow    | Backward  |
|   1500   | Stopped | None      |
|   1600   | Slow    | Forward   |
|   2500   | Fast    | Forward   |

"""

import time
from servo import Servo
from machine import Pin, PWM


# create a PWM servo controller (16 - pin Pico)
# Right wheel
servo_pwm = PWM(Pin(18))
# Left wheel
servo_pwm2 = PWM(Pin(20))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

# create a servo object

my_servo = Servo(
    pwm=servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

my_servo2 = Servo(
    pwm=servo_pwm2, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

def forward():
    my_servo.set_duty(500)
    my_servo2.set_duty(2500)
    time.sleep(2)

def left():
    my_servo.set_duty(1300)
    my_servo2.set_duty(1500)
    time.sleep(2.85)

def right():
    my_servo.set_duty(1500)
    my_servo2.set_duty(1700)
    time.sleep(2.25)

def backward():
    my_servo.set_duty(2500)
    my_servo2.set_duty(500)
    time.sleep(2)

def pause():
    my_servo.set_duty(1500)
    my_servo2.set_duty(1500)
    time.sleep(2)

def stop():
    my_servo.stop()
    my_servo2.stop()
    time.sleep(2)


forward()
left()
right()
right()
backward()
stop()